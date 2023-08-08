from enum import Enum

from pydantic import BaseModel



class MessagePriority(Enum):
    LOW = "low"
    HIGH = "high"


class DeliveryType(Enum):
    EMAIL = "email"
    WEB_SOCKET = "web_socket"


class Event(BaseModel):
    delivery_type: DeliveryType
    message_priority: MessagePriority
