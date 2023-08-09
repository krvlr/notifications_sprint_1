from pydantic import BaseModel, Extra
from typing import Optional


class Body(BaseModel):
    username: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        extra = Extra.allow


class Message(BaseModel):
    transport_type: str
    event: str
    body: Body

    class Config:
        extra = Extra.allow


class WSMessage(BaseModel):
    username: str
    text: str


class SMS(BaseModel):
    number: str
    text: str
