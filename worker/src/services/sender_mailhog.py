import logging
import smtplib
from email.message import EmailMessage

import backoff
from typing import Any

from services.mail_generator import MessageGenerator
from services.sender_base import SenderBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SenderEmailMailhog(SenderBase):
    def __init__(self, host: str, port: int, from_email: str = ""):
        self.host = host
        self.port = port
        self.server = None
        self.from_email = from_email
        self.connect()

    def connect(self):
        if self.server is None:
            logger.info(f"Mailhog {self.host} {str(self.port)}")
            self.server = smtplib.SMTP(self.host, self.port)

    @backoff.on_exception(backoff.expo, exception=(smtplib.SMTPException))
    async def send_message(self, message: Any) -> None:
        mess_gen = MessageGenerator()
        output, subject = mess_gen.generate_email(message)

        to_email = f"{message.body.user_id}@mail.com"
        email_message = EmailMessage()
        email_message["From"] = f"{self.from_email}"
        email_message["To"] = ",".join([f"{to_email}"])
        email_message["Subject"] = f"{subject}!"
        email_message.add_alternative(output, subtype="html")
        receivers = [to_email]

        try:
            if self.server:
                self.server.sendmail(self.from_email, receivers, email_message.as_string())
        except smtplib.SMTPException as exc:
            reason = f"{type(exc).__name__}: {exc}"
            logger.info(f"Не удалось отправить письмо. {reason}. Попытка повторной отправки")
            raise exc
        else:
            logger.info("Письмо отправлено!")
