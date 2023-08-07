from typing import List

from pydantic import Field, Extra

from pydantic_settings import BaseSettings


class WorkerSettings(BaseSettings):
    rabbit_user: str = Field(default="guest", env="RABBITMQ_USER")
    rabbit_password: str = Field(default="guest", env="RABBITMQ_PASS")

    rabbit_host: str = Field(default="notification_rabbitmq", env="RABBITMQ_HOST")
    rabbit_port: int = Field(default=5672, env="RABBITMQ_PORT")

    notif_db_host: str = Field('notification_db', env='DB_HOST')
    notif_db_port: int = Field(5432, env='DB_PORT')
    notif_db_name: str = Field('db_name', env='DB_NAME')
    notif_db_user: str = Field('db_user', env='DB_USER')
    notif_db_password: str = Field('db_password', env='DB_PASSWORD')

    mailhog_host: str = Field('mailhog', env='MAILHOG_HOST')
    mailhog_port: int = Field(1025, env='MAILHOG_PORT')
    using_mailhog: bool = Field(True, env='USING_MAILHOG')

    sender_type: str = Field('Email', env='CONSUMER_TYPE')
    sendgrid_key: str = Field('', env='SENDGRID_KEY')
    from_email: str = Field('ivan@ivan.com', env='FROM_EMAIL')

    # low='low'+settings.consumertype
    routing_keys: List[str] = Field(['low', 'middle', 'high'], env='ROUTING_KEYS')
    ws_host: str = Field('localhost', env='WS_HOST')
    ws_port: int = Field(8765, env='WS_PORT')

    class Config:
        extra = Extra.ignore
        env_file = ".env"


worker_settings = WorkerSettings()
