FROM python:3.10.2

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'config.settings'
ENV PYTHONPATH '/opt/app'

COPY requirements.txt .

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY ./src .

EXPOSE 8000

RUN chmod +x manage.sh
ENTRYPOINT ["./manage.sh"]