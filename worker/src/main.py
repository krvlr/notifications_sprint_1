import asyncio
import logging

import aio_pika

from core.config import worker_settings
from worker_service import create_consumers, Worker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info('Started')
    connection = await aio_pika.connect_robust(
        f"amqp://{worker_settings.rabbit_user}:{worker_settings.rabbit_password}"
        f"@{worker_settings.rabbit_host}:{worker_settings.rabbit_port}/",
    )

    for cons in await create_consumers(connection):
        worker = Worker(cons)
        await worker.run()

    logging.info('Waiting for messages')
    try:
        await asyncio.Future()
    finally:
        await connection.close()

    # queue_name = "low"
    # routing_key = "low"
    #
    # channel = await connection.channel()
    #
    # # await channel.default_exchange.publish(
    # #         aio_pika.Message(body=f"Hello {queue_name}".encode()),
    # #         routing_key=queue_name,
    # # )
    #
    #
    # #queue_name = "high"
    #
    # #channel = await connection.channel()
    #
    # await channel.set_qos(prefetch_count=100)
    #
    # queue = await channel.declare_queue(queue_name, auto_delete=True)
    #
    # await queue.consume(process_message)
    #
    # try:
    #     await asyncio.Future()
    # finally:
    #     await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
