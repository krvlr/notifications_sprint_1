import logging

import aio_pika
import asyncio

from core.config import worker_settings
from worker_service import create_consumers, Worker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info('Started')
    logger.info(f"amqp://{worker_settings.rabbit_user}:{worker_settings.rabbit_password}"
                f"@{worker_settings.rabbit_host}:{worker_settings.rabbit_port}/", )
    connection = await aio_pika.connect_robust(
        f"amqp://{worker_settings.rabbit_user}:{worker_settings.rabbit_password}"
        f"@{worker_settings.rabbit_host}:{worker_settings.rabbit_port}/",
    )

    for cons in await create_consumers(connection):
        worker = Worker(cons)
        await worker.run()

    logging.info('Waiting for rabbit messages')
    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
