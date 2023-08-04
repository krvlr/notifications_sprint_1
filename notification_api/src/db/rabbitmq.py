import aio_pika

from db.base_amqp import AmqpBroker
from models.base import WorkerMessage, MessagePriority


class RabbitMQ(AmqpBroker):
    def __init__(self, exchange: aio_pika.abc.AbstractExchange) -> None:
        self.exchange = exchange

    async def post(
        self,
        priority: MessagePriority,
        message: WorkerMessage,
    ) -> None:
        await self.exchange.publish(
            message=aio_pika.Message(
                body=message.json().encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            ),
            routing_key=priority.value,
        )
