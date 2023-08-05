import json
import os
import smtplib
from abc import ABC, abstractmethod
from typing import Any

from worker.src.core.config import worker_settings
from worker.src.models.message import Message, WSMessage
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import websockets


class SenderBase(ABC):
    @abstractmethod
    async def send_message(self, mess: Any) -> None:
        pass


class SenderEmailMailhog(SenderBase):
    def __init__(self, host: str, port: int, from_email: str = None):
        self.host = host
        self.port = port
        self.server = None
        self.from_email = from_email
        self.connect()

    def connect(self):
        if self.server is None:
            self.server = smtplib.SMTP(self.host, self.port)

    async def send_message(self, mess: Message) -> None:
        current_path = os.path.dirname(__file__)
        loader = FileSystemLoader(current_path)
        env = Environment(loader=loader)

        to_email = f'{mess.body.username}@mail.com'
        subject = mess.event_type
        content = mess.event_type
        if mess.event_type == "user-reporting.v1.registered":
            subject = f'Добро пожаловать, {mess.body.username}'
            content = f'Добро пожаловать!'

        template = env.get_template('mail.html')
        data = {
            'title': f'{subject}',
            'text': f'{content}',
            'image': 'https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg'
        }
        output = template.render(**data)

        message1 = EmailMessage()
        message1["From"] = f'{self.from_email}'
        message1["To"] = ",".join([f'{to_email}'])
        message1["Subject"] = f'{subject}!'
        message1.add_alternative(output, subtype='html')
        receivers = [to_email, ]
        try:
            self.server.sendmail(self.from_email, receivers, message1.as_string())
        except smtplib.SMTPException as exc:
            reason = f'{type(exc).__name__}: {exc}'
            print(f'Не удалось отправить письмо. {reason}')
        else:
            print('Письмо отправлено!')


class SenderEmailSendgrid(SenderBase):
    def __init__(self, host: str, port: int, from_email: str = None):
        self.host = host
        self.port = port
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

        to_email = f'{mess.body.username}@mail.com'
        subject = ''
        content = ''
        if mess.event_type == "user-reporting.v1.registered":
            subject = f'Добро пожаловать, {mess.body.username}'
            content = f'Добро пожаловать!'

        template = env.get_template('mail.html')
        data = {
            'title': f'{subject}',
            'text': f'{content}',
            'image': 'https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg'
        }
        output = template.render(**data)

        message = Mail(
            from_email=self.from_email,
            to_emails=to_email,
            subject=subject,
            html_content=output
        )
        try:
            self.sg.send(message)
        except smtplib.SMTPException as exc:
            reason = f'{type(exc).__name__}: {exc}'
            print(f'Не удалось отправить письмо Sendgrid. {reason}')
        else:
            print('Письмо отправлено Sendgrid!')



class SenderWebsocket(SenderBase):
    def __init__(self, host: str, port: int, token: str, api_url: str):
        self.host = host
        self.port = port
        self.token = token
        self.api_url = api_url

    async def send_message(
        self,
        ws_mess: WSMessage
        # username: str,
        # text: str,
    ) -> None:
        url = 'ws://{host}:{port}/{api}?token={token}'.format(
            host=self.host,
            port=self.port,
            api=self.api_url,
            token=self.token,
        )
        mess = {
            'username': ws_mess.username,
            'text': ws_mess.text,
        }
        async with websockets.connect(url) as websocket:
            await websocket.send(json.dumps(mess))
