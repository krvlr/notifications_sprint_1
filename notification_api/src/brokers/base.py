from abc import ABC, abstractmethod

from models.base import Message, PriorityType


class Broker(ABC):
    @abstractmethod
    async def post(
        self,
        priority: PriorityType,
        message: Message,
    ) -> None:
        pass
