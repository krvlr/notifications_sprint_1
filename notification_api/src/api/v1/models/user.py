import datetime

from pydantic import BaseModel

from api.v1.models.base import Event


class User(BaseModel):
    username: str
    created_at: str


class UserEvent(Event):
    body: User
