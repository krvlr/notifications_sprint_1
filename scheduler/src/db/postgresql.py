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
    def get_notifications(self) -> DictRow:
        """Возвращает список рассылок с датой меньше или равной текущей"""
        with self.conn_context() as conn:
            with conn.cursor() as curs:
                curs.execute(
                    "SELECT schedules.id, schedules.planned_date, schedules.group, "
                    "schedules.template_id, schedules.priority as message_priority, "
                    "schedules.timing, templates.transport_type "
                    "FROM notification.schedules JOIN notification.templates "
                    "ON schedules.template_id = templates.id WHERE schedules.planned_date <= %s",
                    (datetime.now(),),
                )
                while row := curs.fetchone():
                    yield row

    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def update_mailing_date(
        self,
        notification_id: uuid.UUID,
        planned_date: datetime,
    ):
        """Обновляет дату рассылки после отправки в очередь"""
        with self.conn_context() as conn:
            with conn.cursor() as curs:
                curs.execute(
                    "UPDATE notification.schedules SET planned_date = %s WHERE id = %s",
                    (planned_date, str(notification_id)),
                )
