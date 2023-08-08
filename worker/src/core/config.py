from typing import List

from pydantic import Field, Extra

from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    dbname: str = Field(default='db_name', env='DB_NAME')
    user: str = Field(default='db_user', env='DB_USER')
    password: str = Field(default='db_password', env='DB_PASSWORD')
    host: str = Field(default='notification_db', env='DB_HOST')
    port: int = Field(default=5432, env='DB_PORT')

    class Config:
        extra = Extra.ignore
        env_file = '.env'
        env_file_encoding = 'utf-8'


class WorkerSettings(BaseSettings):
    rabbit_user: str = Field(default="guest", env="RABBITMQ_USER")
    rabbit_password: str = Field(default="guest", env="RABBITMQ_PASS")

    rabbit_host: str = Field(default="notification_rabbitmq", env="RABBITMQ_HOST")
    rabbit_port: int = Field(default=5672, env="RABBITMQ_PORT")

    mailhog_host: str = Field(default='mailhog', env='MAILHOG_HOST')
    mailhog_port: int = Field(default=1025, env='MAILHOG_PORT')
    using_mailhog: bool = Field(default=True, env='USING_MAILHOG')

    sender_type: str = Field(default='Email', env='CONSUMER_TYPE')
    sendgrid_key: str = Field(default='', env='SENDGRID_KEY')
    from_email: str = Field(default='ivan@ivan.com', env='FROM_EMAIL')

    # low='low'+settings.consumertype
    routing_keys: List[str] = Field(default=['low', 'middle', 'high'], env='ROUTING_KEYS')
    ws_host: str = Field(default='localhost', env='WS_HOST')
    ws_port: int = Field(default=8765, env='WS_PORT')

    class Config:
        extra = Extra.ignore
        env_file = ".env"


worker_settings = WorkerSettings()
pg_settings = PostgresSettings()
