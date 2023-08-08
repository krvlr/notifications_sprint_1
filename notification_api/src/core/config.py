from pydantic import Field, Extra
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        extra = Extra.ignore
        env_file = ".env"


class ProjectSettings(BaseConfig):
    project_name: str = Field(default="notifications", env="PROJECT_NAME")


class LoggerSettings(BaseConfig):
    debug: bool = Field(default=True, env="DEBUG")
    level: str = Field(default="INFO", env="LOGGING_LEVEL")
    format: str = Field(default="%(asctime)s - %(name)s - %(levelname)s - %(message)s", env="LOG_FORMAT")
    default_handlers: list = ["console"]


class RabbitMQSettings(BaseConfig):
    login: str = Field(default="guest", env="RABBITMQ_DEFAULT_USER")
    password: str = Field(default="guest", env="RABBITMQ_DEFAULT_PASS", repr=False)
    host: str = Field(default="notification_rabbitmq", env="RABBITMQ_HOST")
    port: int = Field(default=5672, env="RABBITMQ_PORT")


project_settings = ProjectSettings()
logger_settings = LoggerSettings()
rabbitmq_settings = RabbitMQSettings()
