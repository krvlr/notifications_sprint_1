import uuid

from pydantic import BaseModel

from api.v1.models.base import Event


class MassMailingModel(BaseModel):
    cohort: str
    template_id: uuid.UUID


class MassMailingEvent(Event):
    body: MassMailingModel
