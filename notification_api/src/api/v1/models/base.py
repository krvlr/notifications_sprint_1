from pydantic import BaseModel

from models.base import DeliveryType, PriorityType


class Event(BaseModel):
    delivery_type: DeliveryType
    priority: PriorityType
