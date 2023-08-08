from contextlib import contextmanager

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor


@contextmanager
def get_cursor(connection):
    cur = connection.cursor()
    try:
        yield cur
    finally:
        cur.close()


#@backoff()
def create_conn(connection_param):
    return psycopg2.connect(**connection_param, cursor_factory=DictCursor)


@contextmanager
def get_pg_conn(connection_param):
    try:
        con = create_conn(connection_param)
        yield con
    finally:
        con.close()


class PostgresExtractor:
    def __init__(self, pg_connection: _connection):
        self.pg_connection = pg_connection

    def get_template_by_id(self, template_id: str):
        with get_cursor(self.pg_connection) as cursor:
            stmt = """
                SELECT template_body FROM notification.templates
                WHERE id = %s
                """
            data = [template_id, ]
            cursor.execute(stmt, data)
            template = cursor.fetchone()
            return template
