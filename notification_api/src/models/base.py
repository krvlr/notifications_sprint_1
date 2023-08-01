import enum

from pydantic import BaseModel


class DeliveryType(str, enum.Enum):  # noqa: WPS600
    EMAIL = "email"
    WEB_SOCKET = "websocket"


class EventType(enum.Enum):
    REVIEW_RATED = "review-reporting.v1.rated"
    USER_REGISTERED = "user-reporting.v1.registered"
    ADMIN = "admin-reporting.v1.event"


class PriorityType(enum.Enum):
    LOW = "low"
    HIGH = "high"


class Message(BaseModel):
    delivery_type: DeliveryType
    event_type: EventType
    body: BaseModel
