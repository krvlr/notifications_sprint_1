from abc import ABC, abstractmethod

from models.base import WorkerMessage, MessagePriority


class AmqpBroker(ABC):
    @abstractmethod
    async def post(self, priority: MessagePriority, message: WorkerMessage) -> None:
        pass