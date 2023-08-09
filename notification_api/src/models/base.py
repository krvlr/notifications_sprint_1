from enum import Enum

from pydantic import BaseModel, typing

from api.v1.models.base import TransportType


class Event(Enum):
    REVIEW_RATED = "review.rated"
    USER_REGISTERED = "user.registered"
    MASS_MAILING = "mass.mailing"


class WorkerMessage(BaseModel):
    transport_type: TransportType
    event: Event
    body: typing.Any
