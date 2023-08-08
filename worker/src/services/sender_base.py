import logging

from abc import ABC, abstractmethod
from typing import Any


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SenderBase(ABC):
    @abstractmethod
    async def send_message(self, mess: Any) -> None:
        pass


