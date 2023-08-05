from enum import Enum

from pydantic import BaseModel


class MessagePriority(Enum):
    LOW = "low"
    HIGH = "high"


class DeliveryType(Enum):
    EMAIL = "email"
    WEB_SOCKET = "web_socket"


class Event(Enum):
    REVIEW_RATED = "review.rated"
    USER_REGISTERED = "user.registered"
    ADMIN = "admin.event"


class WorkerMessage(BaseModel):
    delivery_type: DeliveryType
    event: Event
    body: BaseModel
