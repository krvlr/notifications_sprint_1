import uuid
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Timing(Enum):
    ONE = "one"
    WEEK = "week"
    MONTH = "month"


class TransportType(Enum):
    EMAIL = "email"
    WEBSOCKET = "websocket"


class MessagePriority(Enum):
    LOW = "low"
    MIDDLE = "middle"
    HIGH = "high"


class MassMailingEvent(BaseModel):
    id: uuid.UUID
    planned_date: datetime
    group: str
    template_id: uuid.UUID
    message_priority: MessagePriority
    timing: Timing
    transport_type: TransportType
