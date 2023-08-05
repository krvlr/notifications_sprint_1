from pydantic import Field


from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"


class WorkerSettings(BaseConfig):
    rabbit_user: str = Field(default="guest", env="RABBITMQ_USER")
    rabbit_password: str = Field(default="guest", env="RABBITMQ_PASS")
    rabbit_host: str = Field(default="localhost", env="RABBITMQ_HOST")
    rabbit_port: int = Field(default=5672, env="RABBITMQ_PORT")

    notif_db_host: str = Field('localhost', env='DB_HOST')
    notif_db_port: int = Field(5432, env='DB_PORT')
    notif_db_name: str = Field('db_name', env='DB_NAME')
    notif_db_user: str = Field('db_user', env='DB_USER')
    notif_db_password: str = Field('db_password', env='DB_PASSWORD')

    mailhog_host: str = Field('localhost', env='MAILHOG_HOST')
    mailhog_port: int = Field(1025, env='MAILHOG_PORT')
    using_mailhog: bool = Field(True, env='USING_MAILHOG')

    consumer_type: str = Field('Email', env='CONSUMER_TYPE')
    sendgrid_key: str = Field('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', env='SENDGRID_KEY')


worker_settings = WorkerSettings()
