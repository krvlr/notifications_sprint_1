from pydantic import Field, Extra
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        extra = Extra.ignore
        env_file = ".env"


class ApiSettings(BaseConfig):
    host: str = Field(default="api-notification", env="NOTIFICATION_API_HOST")
    port: int = Field(default=8000, env="NOTIFICATION_API_PORT")


class PostgresSettings(BaseConfig):
    user: str = Field(default="db_user", env="DB_USER")
    password: str = Field(default="db_password", env="DB_PASSWORD")
    host: str = Field(default="notification_db", env="DB_HOST")
    port: int = Field(default=5432, env="DB_PORT")
    dbname: str = Field(default="db_name", env="DB_NAME")


api_settings = ApiSettings()
postgres_settings = PostgresSettings()
