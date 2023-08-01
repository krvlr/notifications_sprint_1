from pydantic import BaseSettings, Field, Required


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"


class LoggerSettings(BaseConfig):
    debug: str = Field(default="True", env="DEBUG")
    level: str = Field(default="INFO", env="LOGGING_LEVEL")
    format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s", env="LOG_FORMAT"
    )
    default_handlers: list = ["console"]


class ProjectSettings(BaseConfig):
    project_name: str = Field(default="notifications", env="PROJECT_NAME")


class RabbitMQSettings(BaseConfig):
    username: str = Field(Required, env="RABBITMQ_USER")
    password: str = Field(Required, env="RABBITMQ_PASS")
    host: str = Field("127.0.0.1", env="RABBITMQ_HOST")
    port: int = Field(default=5672, env="RABBITMQ_PORT")


base_settings = BaseSettings()
logger_settings = LoggerSettings()
project_settings = ProjectSettings()
rabbitmq_settings = RabbitMQSettings()
