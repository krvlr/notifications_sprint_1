from typing_extensions import Any

from core.config import pg_settings
from db.postgres_extractor import PostgresExtractor
from db.postgres_extractor import get_pg_conn
from jinja2 import Environment, FunctionLoader

REVIEW_RATED = "review.rated"
USER_REGISTERED = "user.registered"
ADMIN = "admin.event"

WELCOME_TEMPLATE_ID = "d901cd22-4cc1-4d62-a6ab-0c2f39478798"


class MessageGenerator:
    def generate_email(self, message: Any):
        if message.event == USER_REGISTERED:
            return self.generate_welcome_mail(message)
        elif message.event == REVIEW_RATED:
            return self.generate_rating_mail(message)
        elif message.event == ADMIN:
            return self.generate_mass_sending_mail(message)

    def get_template_func(self, name: str):
        if name == "welcome.html":
            template_id = WELCOME_TEMPLATE_ID
        elif name == "rating.html":
            template_id = WELCOME_TEMPLATE_ID
        else:
            template_id = WELCOME_TEMPLATE_ID
        with get_pg_conn(pg_settings.dict()) as pg_conn:
            postgres_extractor = PostgresExtractor(pg_conn)
            template_body = postgres_extractor.get_template_by_id(template_id)
            return template_body[0]

    def generate_welcome_mail(self, message: Any):
        loader = FunctionLoader(self.get_template_func)
        env = Environment(loader=loader)

        subject = f"Добро пожаловать, {message.body.user_id}"
        content = "Добро пожаловать!"

        template = env.get_template("welcome.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)
        return output, subject

    def generate_rating_mail(self, message: Any):
        loader = FunctionLoader(self.get_template_func)
        env = Environment(loader=loader)

        subject = f"Вашему обзору поставили оценку, {message.body.user_id}"
        content = "Вашему обзору поставили оценку!"

        template = env.get_template("rating.html")
        data = {
            "title": f"{subject}",
            "text": f"{content}",
            "image": "https://pictures.s3.yandex.net:443/resources/news_1682073799.jpeg",
        }
        output = template.render(**data)
        return output, subject

    def generate_mass_sending_mail(self, message: Any):
        loader = FunctionLoader(self.get_template_func)
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
