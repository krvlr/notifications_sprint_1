import asyncio
import logging

import aio_pika

from models.message import Message
from db.sender import SenderBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConsumerRabbitMQ:
    def __init__(
        self,
        queue: aio_pika.abc.AbstractQueue,
        delay: int,
        sender: SenderBase
    ) -> None:
        self.queue = queue
        self.delay = delay
        self.sender = sender

    async def process_message(
        self,
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        await asyncio.sleep(self.delay)
        logger.info(message.body.decode())
        try:
            mess = Message.model_validate_json(message.body.decode())
            await self.sender.send_message(mess)
        except:
            logger.error(f'Validation error message {message.body.decode()}')
        await message.ack()

    async def consume_c(self) -> None:
        await self.queue.consume(self.process_message)
