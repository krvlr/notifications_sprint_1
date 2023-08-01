import aio_pika
from models.base import Message, PriorityType

from brokers.base import Broker


class RabbitMQ(Broker):
    def __init__(self, exchange: aio_pika.abc.AbstractExchange) -> None:
        self.exchange = exchange

    async def post(
        self,
        priority: PriorityType,
        message: Message,
    ) -> None:
        pika_message = aio_pika.Message(
            body=message.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await self.exchange.publish(
            message=pika_message,
            routing_key=priority.value,
        )
