import logging

import backoff
import requests
from requests.exceptions import ConnectionError

from core.config import api_settings


class DeliveryApiClient(object):
    @backoff.on_exception(wait_gen=backoff.expo, exception=Exception)
    def send(self, delivery_type, cohort, template_id, subject, priority):
        """Отправить запланированную рассылку на обработку"""
        body = {
            "delivery_type": delivery_type,
            "priority": priority,
            "body": {"cohort": cohort, "template_id": str(template_id), "subject": subject},
        }
        url = f"http://{api_settings.host}:{api_settings.port}/api/v1/admin/"
        try:
            return requests.post(url, json=body)
        except ConnectionError as err:
            logging.error(f"Попытка соединения {url}")
            raise ConnectionError(err)
