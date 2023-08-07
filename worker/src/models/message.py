from pydantic import BaseModel
from typing import Optional


class Body(BaseModel):
    username: str
    created_at: str


class Message(BaseModel):
    delivery_type: str
    event_type: str
    body: Body


class WSMessage(BaseModel):
    username: str
    text: str


class SMS(BaseModel):
    number: str
    text: str
