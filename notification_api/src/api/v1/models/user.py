import uuid

from pydantic import BaseModel

from api.v1.models.base import Event


class User(BaseModel):
    user_id: uuid.UUID
    created_at: str


class UserEvent(Event):
    body: User
