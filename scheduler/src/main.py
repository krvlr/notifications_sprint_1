import http
import logging
import time
from datetime import datetime

from dateutil.relativedelta import relativedelta

from api_client import ApiClient
from db.postgresql import PostgresStorage
from models.mailing import MassMailingEvent, Timing

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_next_date(current_planed_date: datetime, timing: Timing) -> datetime | None:
    if timing == Timing.ONE:
        return None
    timing_relativedelta_mapping = {Timing.WEEK: "weeks", Timing.MONTH: "months"}
    return current_planed_date + relativedelta(**{timing_relativedelta_mapping[timing]: 1})  # type: ignore


storage = PostgresStorage()
api_client = ApiClient()

if __name__ == "__main__":
    logger.info("Scheduler starting")

    while True:
        time.sleep(1)

        mass_mailing_events = storage.get_notifications()

        for event in mass_mailing_events:
            mass_mailing_event = MassMailingEvent(**event)

            logger.info(
                f"Process message for mass mailing {mass_mailing_event.model_json_schema()}"
            )

            next_date = get_next_date(
                mass_mailing_event.planned_date,
                mass_mailing_event.timing,
            )

            response = api_client.post_mass_mailing(
                transport_type=mass_mailing_event.transport_type.value,
                cohort=mass_mailing_event.group,
                template_id=mass_mailing_event.template_id,
                message_priority=mass_mailing_event.message_priority.value,
            )

            if response.status_code == http.HTTPStatus.OK:
                storage.update_mailing_date(
                    mass_mailing_event.id,
                    next_date,
                )
