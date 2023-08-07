import aio_pika

from core.config import worker_settings
from db.rabbitmq import ConsumerRabbitMQ
from db.sender import SenderEmailMailhog, SenderEmailSendgrid, SenderWebsocket


async def get_queue(
    connection: aio_pika.abc.AbstractRobustConnection,
    routing_key: str,
) -> aio_pika.abc.AbstractQueue:
    channel = await connection.channel()
    return await channel.declare_queue(
        name=routing_key,
        durable=True,
    )


async def create_consumers(
    connection: aio_pika.abc.AbstractRobustConnection,
):
    consumers = []

    for routing_key in worker_settings.routing_keys:
        queue = await get_queue(connection, routing_key)

        if worker_settings.sender_type == 'Email':
            if worker_settings.using_mailhog:
                sender = SenderEmailMailhog(host=worker_settings.mailhog_host,
                                            port=worker_settings.mailhog_port,
                                            from_email=worker_settings.from_email)
            else:
                sender = SenderEmailSendgrid(from_email=worker_settings.from_email)
        elif worker_settings.sender_type == 'Websocket':
            sender = SenderWebsocket(host=worker_settings, port=worker_settings.ws_port)
        else:
            sender = SenderEmailMailhog(host=worker_settings.mailhog_host,
                                        port=worker_settings.mailhog_port,
                                        from_email=worker_settings.from_email)

        consumers.append(ConsumerRabbitMQ(queue, 0, sender))
    return consumers


class Worker:
    def __init__(self, consumer: ConsumerRabbitMQ) -> None:
        self.consumer = consumer

    async def run(self) -> None:
        await self.consumer.consume_c()

# TODO генераторы писем и получение темплейтов из постгры, укорачиватель ссылоку, сервис авторизации
