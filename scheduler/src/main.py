import http
import logging
import time
from datetime import datetime

from dateutil.relativedelta import relativedelta

from delivery_api_client import DeliveryApiClient
from models.mailing import AdminEvent, Periodicity
from db.postgresql import PostgresStorage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_next_date(current_planed_date: datetime, periodicity: str) -> datetime | None:
    if periodicity == Periodicity.once.value:
        return None
    mapping = {
        Periodicity.daily.value: "days",
        Periodicity.weekly.value: "weeks",
        Periodicity.monthly.value: "months",
    }
    return current_planed_date + relativedelta(**{mapping[periodicity]: 1})  # type: ignore


storage = PostgresStorage()
api_client = DeliveryApiClient()

if __name__ == "__main__":
    while True:
        admin_events = storage.get_pending_notifications()

        for event in admin_events:
            admin_event = AdminEvent(**event)
            next_date = get_next_date(
                admin_event.next_planned_date,
                admin_event.periodicity.value,
            )

            response = api_client.send(
                delivery_type=admin_event.channel.value,
                cohort=admin_event.user_group,
                template_id=admin_event.template_id,
                subject=admin_event.subject,
                priority=admin_event.priority.value,
            )
            if response.status_code == http.HTTPStatus.OK:
                storage.update_processed_notifications(
                    admin_event.id,
                    next_date,
                )
            time.sleep(1)
