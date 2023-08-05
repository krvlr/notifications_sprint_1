import aio_pika

from db.rabbitmq import ConsumerRabbitMQ
from worker.src.core.config import worker_settings
from worker.src.db.sender import SenderEmailMailhog


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
    #low='low'+settings.consumertype
    queue_names = ['low', 'middle', 'high']
    for queue_name in queue_names:
        queue = await get_queue(connection, queue_name)
        consumers.append(ConsumerRabbitMQ(queue, 1, SenderEmailMailhog(host=worker_settings.mailhog_host,
                                                                       port=worker_settings.mailhog_port,
                                                                       from_email="ivan@ivan.com")))
    return consumers


class Worker:
    def __init__(self, consumer: ConsumerRabbitMQ) -> None:
        self.consumer = consumer

    async def run(self) -> None:
        await self.consumer.consume_c()

#TODO добавить ws нормально, сделать разные сендеры в зависимости от настроек енв, генераторы писем и получение темплейтов из постгры, укорачиватель ссылоку, сервис авторизации