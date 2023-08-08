import os

from core.config import pg_settings
from db.postgres_extractor import PostgresExtractor
from db.postgres_extractor import get_pg_conn
from jinja2 import Environment, FileSystemLoader, FunctionLoader

REVIEW_RATED = "review.rated"
USER_REGISTERED = "user.registered"
ADMIN = "admin.event"

WELCOME_TEMPLATE_ID = 'deb23acb-89e4-42f0-9b2d-97e62ce828e9'


class MessageGenerator:
    def generate_email(self, mess):
        if mess.event == USER_REGISTERED:
            return self.generate_welcome_mail(mess)
        elif mess.event == REVIEW_RATED:
            return self.generate_rating_mail(mess)
        elif mess.event == ADMIN:
            return self.generate_mass_sending_mail(mess)

    def get_template_func(self, name):
        if name == 'welcome.html':
            template_id = WELCOME_TEMPLATE_ID
        elif name == 'rating.html':
            template_id = WELCOME_TEMPLATE_ID
        else:
            template_id = WELCOME_TEMPLATE_ID
        with get_pg_conn(pg_settings.dict()) as pg_conn:
            postgres_extractor = PostgresExtractor(pg_conn)
            template_body = postgres_extractor.get_template_by_id(template_id)
            return template_body[0]

    def generate_welcome_mail(self, mess):
        loader = FunctionLoader(self.get_template_func)
        env = Environment(loader=loader)

        subject = f'Добро пожаловать, {mess.body.username}'
        content = f'Добро пожаловать!'

        template = env.get_template_func('welcome.html')
        data = {
            'title': f'{subject}',
            'text': f'{content}',
            'image': 'https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg'
        }
        output = template.render(**data)
        return output, subject

    def generate_rating_mail(self, mess):
        loader = FunctionLoader(self.get_template_func)
        env = Environment(loader=loader)

        subject = f'Вашему обзору поставили оценку, {mess.body.username}'
        content = f'Вашему обзору поставили оценку!'

        template = env.get_template_by_id('rating.html')
        data = {
            'title': f'{subject}',
            'text': f'{content}',
            'image': 'https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg'
        }
        output = template.render(**data)
        return output, subject

    def generate_mass_sending_mail(self, mess):
        loader = FunctionLoader(self.get_template_func)
        env = Environment(loader=loader)

        subject = f'Массовая рассылка'
        content = f'Массовая рассылка!'

        template = env.get_template_by_id('mail.html')
        data = {
            'title': f'{subject}',
            'text': f'{content}',
            'image': 'https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg'
        }
        output = template.render(**data)
        return output, subject
