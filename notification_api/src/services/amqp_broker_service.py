from typing import Union

import aio_pika
import backoff
from pamqp.exceptions import AMQPFrameError

from db.base_amqp import AmqpBroker
from db.rabbitmq import RabbitMQ
from core.config import rabbitmq_settings
from models.base import MessagePriority

amqp_broker: Union[AmqpBroker, None] = None
rabbitmq_connection: Union[aio_pika.abc.AbstractConnection, None] = None


@backoff.on_exception(backoff.expo, exception=(ConnectionError, AMQPFrameError))
async def connect() -> None:
    global amqp_broker, rabbitmq_connection

    rabbitmq_connection = await aio_pika.connect_robust(
        host=rabbitmq_settings.host,
        port=rabbitmq_settings.port,
        login=rabbitmq_settings.login,
        password=rabbitmq_settings.password,
    )

    channel = await rabbitmq_connection.channel()

    for priority in MessagePriority:
        await channel.declare_queue(
            name=priority.value,
            durable=True,
        )

    amqp_broker = RabbitMQ(exchange=channel.default_exchange)


async def disconnect() -> None:
    if rabbitmq_connection is not None:
        await rabbitmq_connection.close()


def get_amqp_broker() -> AmqpBroker:
    return amqp_broker
