from typing import Union

import aio_pika
import backoff
from pamqp.exceptions import AMQPFrameError

from brokers.base import Broker
from brokers.rabbitmq import RabbitMQ
from core.config import rabbitmq_settings
from models.base import PriorityType

broker: Union[Broker, None] = None
connection: Union[aio_pika.abc.AbstractConnection, None] = None


@backoff.on_exception(
    backoff.expo,
    exception=(ConnectionError, AMQPFrameError),
)
async def connect() -> None:
    global broker, connection  # noqa: WPS100, WPS420

    connection = await aio_pika.connect_robust(
        "amqp://{username}:{password}@{host}:{port}".format(
            **rabbitmq_settings.dict(),
        ),
    )
    channel = await connection.channel()
    for priority in PriorityType:
        await channel.declare_queue(
            name=priority.value,
            durable=True,
        )

    broker = RabbitMQ(exchange=channel.default_exchange)


async def disconnect() -> None:
    if connection is not None:
        await connection.close()


def get_broker() -> Union[Broker, None]:
    return broker
