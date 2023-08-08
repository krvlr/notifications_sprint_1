from enum import Enum

from pydantic import BaseModel

from api.v1.models.user import User

from api.v1.models.review import ReviewRating

from api.v1.models.base import DeliveryType


class Event(Enum):
    REVIEW_RATED = "review.rated"
    USER_REGISTERED = "user.registered"
    ADMIN = "admin.event"


class WorkerMessage(BaseModel):
    delivery_type: DeliveryType
    event: Event
    body: User | ReviewRating
