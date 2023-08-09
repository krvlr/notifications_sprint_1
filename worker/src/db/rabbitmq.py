import logging

import aio_pika

from models.message import Message
from services.sender_base import SenderBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConsumerRabbitMQ:
    def __init__(self, queue: aio_pika.abc.AbstractQueue, sender: SenderBase) -> None:
        self.queue = queue
        self.sender = sender

    async def process_message(
        self,
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        logger.info(message.body.decode())
        try:
            mess = Message.model_validate_json(message.body.decode())
            await self.sender.send_message(mess)
        except Exception as ex:
            logger.error(f"Exception processing rabbit message {message.body.decode()} {ex}")
        await message.ack()

    async def consume_c(self) -> None:
        await self.queue.consume(self.process_message)
