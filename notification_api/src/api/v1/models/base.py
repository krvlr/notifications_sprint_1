from enum import Enum

from pydantic import BaseModel


class MessagePriority(Enum):
    LOW = "low"
    MIDDLE = "middle"
    HIGH = "high"


class TransportType(Enum):
    EMAIL = "email"
    WEB_SOCKET = "websocket"


class Event(BaseModel):
    transport_type: TransportType
    message_priority: MessagePriority
