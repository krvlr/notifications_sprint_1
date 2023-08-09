import aio_pika

from api.v1.models.base import MessagePriority
from db.base_amqp import AmqpBroker
from models.base import WorkerMessage


class RabbitMQ(AmqpBroker):
    def __init__(self, exchange: aio_pika.abc.AbstractExchange) -> None:
        self.exchange = exchange

    async def post(
        self,
        message_priority: MessagePriority,
        message: WorkerMessage,
    ) -> None:
        await self.exchange.publish(
            message=aio_pika.Message(
                body=message.model_dump_json().encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            ),
            routing_key=message_priority.value,
        )
