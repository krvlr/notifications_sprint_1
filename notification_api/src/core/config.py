import logging
import os

from pydantic import BaseSettings, Field


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"


class BaseSettings(BaseConfig):
    project_name: str = Field(default="notifications", env="PROJECT_NAME")


class LoggerSettings(BaseConfig):
    debug: str = Field(default="True", env="DEBUG")
    level: str = Field(default="INFO", env="LOGGING_LEVEL")
    format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s", env="LOG_FORMAT"
    )
    default_handlers: list = ["console"]


class NotificationSettings(BaseConfig):
    notif_db_host: str = Field(default="127.0.0.1", env="NOTIF_POSTGRES_HOST")
    notif_db_port: str = Field(default="5432", env="NOTIF_POSTGRES_PORT")
    notif_db_name: str = Field(default="5432", env="NOTIF_POSTGRES_NAME")
    notif_db_user: str = Field(default="5432", env="NOTIF_POSTGRES_USER")
    notif_db_password: str = Field(default="5432", env="NOTIF_POSTGRES_PASSWORD")


base_settings = BaseSettings()
logger_settings = LoggerSettings()
notification_settings = NotificationSettings()
