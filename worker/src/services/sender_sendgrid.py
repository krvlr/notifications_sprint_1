import logging
import os
import smtplib

import backoff
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from core.config import worker_settings
from services.sender_base import SenderBase
from models.message import Message
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SenderEmailSendgrid(SenderBase):
    def __init__(self, from_email: str = ""):
        self.sg = None
        self.from_email = from_email
        self.connect()

    def connect(self):
        if self.sg is None:
            self.sg = SendGridAPIClient(worker_settings.sendgrid_key)

    @backoff.on_exception(backoff.expo, exception=(smtplib.SMTPException))
    async def send_message(self, mess: Message) -> None:
        current_path = os.path.dirname(__file__)
        loader = FileSystemLoader(current_path)
        env = Environment(loader=loader)

        to_email = f"{mess.body.user_id}@mail.com"
        subject = ""
        content = ""
        if mess.event_type == "user-reporting.v1.registered":
            subject = f"Добро пожаловать, {mess.body.user_id}"
            content = "Добро пожаловать!"

        template = env.get_template("mail.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)

        message = Mail(
            from_email=self.from_email, to_emails=to_email, subject=subject, html_content=output
        )
        try:
            if self.sg:
                self.sg.post_mass_mailing(message)
        except smtplib.SMTPException as exc:
            reason = f"{type(exc).__name__}: {exc}"
            logger.info(
                f"Не удалось отправить письмо Sendgrid. {reason}. Попытка повторной отправки"
            )
            raise exc
        else:
            logger.info("Письмо отправлено Sendgrid!")
