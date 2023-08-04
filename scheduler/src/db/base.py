import uuid
from abc import ABC, abstractmethod
from datetime import datetime


class Storage(ABC):
    @abstractmethod
    def get_pending_notifications(self):
        pass

    @abstractmethod
    def update_processed_notifications(
        self,
        notification_id: uuid.UUID,
        next_date: datetime,
    ):
        pass
