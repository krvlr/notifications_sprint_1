import uuid

from pydantic import BaseModel

from api.v1.models.base import Event


class AdminModel(BaseModel):
    cohort: str
    subject: str
    template_id: uuid.UUID


class AdminEvent(Event):
    body: AdminModel