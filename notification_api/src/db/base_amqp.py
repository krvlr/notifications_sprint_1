from abc import ABC, abstractmethod

from models.base import WorkerMessage
from api.v1.models.base import MessagePriority


class AmqpBroker(ABC):
    @abstractmethod
    async def post(
        self,
        message_priority: MessagePriority,
        message: WorkerMessage,
    ) -> None:
        pass
