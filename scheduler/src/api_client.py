import logging

import backoff
import requests
from requests.exceptions import ConnectionError

from core.config import api_settings


class ApiClient:
    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def post_mass_mailing(self, transport_type, cohort, template_id, message_priority):
        body = {
            "transport_type": transport_type,
            "message_priority": message_priority,
            "body": {"cohort": cohort, "template_id": str(template_id)},
        }
        url = f"http://{api_settings.host}:{api_settings.port}/api/v1/mass/mass_mailing"
        try:
            return requests.post(url, json=body)
        except ConnectionError as err:
            logging.error(f"Попытка соединения {url}")
            raise ConnectionError(err)
