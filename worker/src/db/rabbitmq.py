import asyncio
import logging

import aio_pika

from worker.src.models.message import Message
from worker.src.db.sender import SenderBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# async def process_message(
#     message: aio_pika.abc.AbstractIncomingMessage,
# ) -> None:
#     async with message.process():
#         print(message.body)
#         await asyncio.sleep(1)


class ConsumerRabbitMQ:
    def __init__(
        self,
        queue: aio_pika.abc.AbstractQueue,
        consumption_delay: int,
        sender: SenderBase
    ) -> None:
        self.queue = queue
        self.consumption_delay = consumption_delay
        self.sender = sender

    async def process_message(
        self,
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        await asyncio.sleep(self.consumption_delay)
        logger.info(message.body.decode())
        mess = Message.model_validate_json(message.body.decode())
        logger.info(mess)
        await self.sender.send_message(mess)
        await message.ack()

    async def consume_c(self) -> None:
        await self.queue.consume(self.process_message)
