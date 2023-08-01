import uuid

from pydantic import BaseModel

from api.v1.models.base import Event


class AdminModel(BaseModel):
    cohort: str
    template_id: uuid.UUID
    subject: str


class AdminEvent(Event):
    body: AdminModel
