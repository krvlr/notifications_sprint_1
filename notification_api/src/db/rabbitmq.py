import json

import aio_pika

from db.base_amqp import AmqpBroker
from models.base import WorkerMessage
from api.v1.models.base import MessagePriority


class RabbitMQ(AmqpBroker):
    def __init__(self, exchange: aio_pika.abc.AbstractExchange) -> None:
        self.exchange = exchange

    async def post(
        self,
        priority: MessagePriority,
        message: WorkerMessage,
    ) -> None:
        mess = aio_pika.Message(
            body=message.json().encode(),
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        print(f'{message.json().encode()}')
        await self.exchange.publish(
            message=mess,
            routing_key=priority.value,
        )
