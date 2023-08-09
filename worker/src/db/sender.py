import json
import logging
import os
import smtplib
from abc import ABC, abstractmethod
from typing import Any

from core.config import worker_settings
from models.message import Message, WSMessage
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import websockets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REVIEW_RATED = "review.rated"
USER_REGISTERED = "user.registered"
ADMIN = "admin.event"


class MessageGenerator:
    def generate_email(self, message: Any):
        if message.event == USER_REGISTERED:
            return self.generate_welcome_mail(message)
        elif message.event == REVIEW_RATED:
            return self.generate_rating_mail(message)
        elif message.event == ADMIN:
            return self.generate_mass_sending_mail(message)

    @staticmethod
    def generate_welcome_mail(message: Any):
        current_path = os.path.dirname(__file__)
        loader = FileSystemLoader(current_path)
        env = Environment(loader=loader)

        subject = f"Добро пожаловать, {message.body.user_id}"
        content = "Добро пожаловать!"

        template = env.get_template("mail.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)
        return output, subject

    @staticmethod
    def generate_rating_mail(message: Any):
        current_path = os.path.dirname(__file__)
        loader = FileSystemLoader(current_path)
        env = Environment(loader=loader)

        subject = f"Вашему обзору поставили оценку, {message.body.user_id}"
        content = "Вашему обзору поставили оценку!"

        template = env.get_template("mail.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)
        return output, subject

    @staticmethod
    def generate_mass_sending_mail(message: Any):
        current_path = os.path.dirname(__file__)
        loader = FileSystemLoader(current_path)
        env = Environment(loader=loader)

        subject = "Массовая рассылка"
        content = "Массовая рассылка!"

        template = env.get_template("mail.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)
        return output, subject


class SenderBase(ABC):
    @abstractmethod
    async def send_message(self, mess: Any) -> None:
        pass


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

    async def send_message(self, message: Any) -> None:
        output, subject = MessageGenerator.generate_welcome_mail(message)

        to_email = f"{message.body.user_id}@mail.com"
        email_message = EmailMessage()
        email_message["From"] = f"{self.from_email}"
        email_message["To"] = ",".join([f"{to_email}"])
        email_message["Subject"] = f"{subject}!"
        email_message.add_alternative(output, subtype="html")
        receivers = [
            to_email,
        ]

        try:
            if self.server:
                self.server.sendmail(self.from_email, receivers, email_message.as_string())
        except smtplib.SMTPException as exc:
            reason = f"{type(exc).__name__}: {exc}"
            print(f"Не удалось отправить письмо. {reason}")
        else:
            print("Письмо отправлено!")


class SenderEmailSendgrid(SenderBase):
    def __init__(self, from_email: str = ""):
        self.sg = None
        self.from_email = from_email
        self.connect()

    def connect(self):
        if self.sg is None:
            self.sg = SendGridAPIClient(worker_settings.sendgrid_key)

    async def send_message(self, mess: Message) -> None:
        current_path = os.path.dirname(__file__)
        loader = FileSystemLoader(current_path)
        env = Environment(loader=loader)

        to_email = f"{mess.body.user_id}@mail.com"
        subject = ""
        content = ""
        if mess.event == "user-reporting.v1.registered":
            subject = f"Добро пожаловать, {mess.body.user_id}"
            content = "Добро пожаловать!"

        template = env.get_template("mail.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)

        message = Mail(from_email=self.from_email, to_emails=to_email, subject=subject, html_content=output)
        try:
            if self.sg:
                self.sg.post_mass_mailing(message)
        except smtplib.SMTPException as exc:
            reason = f"{type(exc).__name__}: {exc}"
            print(f"Не удалось отправить письмо Sendgrid. {reason}")
        else:
            print("Письмо отправлено Sendgrid!")


class SenderWebsocket(SenderBase):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def send_message(self, ws_mess: WSMessage) -> None:
        # ws_server = websockets.serve(receiver, "localhost", 8765)

        uri = f"ws://{self.host}:{self.port}/"
        mess = {
            "username": ws_mess.user_id,
            "text": ws_mess.text,
        }
        async with websockets.connect(uri) as websocket:
            await websocket.post_mass_mailing(json.dumps(mess))
