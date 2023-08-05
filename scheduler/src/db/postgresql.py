import uuid
from contextlib import contextmanager
from datetime import datetime

from db.base import Storage

import backoff
import psycopg2
from core.config import postgres_settings
from psycopg2.extensions import connection
from psycopg2.extras import DictCursor, DictRow


class PostgresStorage(Storage):
    @contextmanager
    def conn_context(self) -> connection:
        connection_ = psycopg2.connect(
            user=postgres_settings.user,
            password=postgres_settings.password,
            host=postgres_settings.host,
            port=postgres_settings.port,
            dbname=postgres_settings.dbname,
            cursor_factory=DictCursor,
        )
        yield connection_
        connection_.commit()
        connection_.close()

    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def get_pending_notifications(self) -> DictRow:
        """Возвращает список рассылок с датой меньше или равной текущей"""
        query = (
            "SELECT ns.id, ns.next_planned_date, ns.periodicity, "
            "ns.user_group, ns.template_id, nt.subject, nt.channel, "
            "ns.priority FROM notifications_scheduledmailing AS ns "
            "JOIN notifications_template AS nt "
            "ON ns.template_id = nt.id WHERE next_planned_date <= %s"
        )
        with self.conn_context() as conn:
            with conn.cursor() as curs:
                curs.execute(query, (datetime.now(),))
                while row := curs.fetchone():
                    yield row

    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def update_processed_notifications(
        self,
        notification_id: uuid.UUID,
        next_date: datetime,
    ):
        """Обновляет запланированную дату рассылки после отправки в очередь"""
        query = "UPDATE notifications_scheduledmailing " + "SET next_planned_date = %s WHERE id = %s"
        with self.conn_context() as conn:
            with conn.cursor() as curs:
                curs.execute(query, (str(next_date), str(notification_id)))
