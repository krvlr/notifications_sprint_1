import uuid
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Periodicity(Enum):
    once = "once"
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"


class TransportType(Enum):
    email = "email"
    websocket = "websocket"


class MessagePriority(Enum):
    LOW = "low"
    HIGH = "high"


class AdminEvent(BaseModel):
    id: uuid.UUID
    user_group: str
    template_id: uuid.UUID
    subject: str
    channel: TransportType
    periodicity: Periodicity
    priority: MessagePriority
    next_planned_date: datetime
