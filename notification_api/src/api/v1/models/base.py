from pydantic import BaseModel

from models.base import DeliveryType, MessagePriority


class Event(BaseModel):
    delivery_type: DeliveryType
    message_priority: MessagePriority
