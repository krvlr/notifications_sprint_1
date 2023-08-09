import uuid
from abc import ABC, abstractmethod
from datetime import datetime


class Storage(ABC):
    @abstractmethod
    def get_notifications(self):
        pass

    @abstractmethod
    def update_mailing_date(
        self,
        notification_id: uuid.UUID,
        next_date: datetime,
    ):
        pass
