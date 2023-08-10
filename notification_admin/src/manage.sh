#!/bin/bash
CONTAINER_FIRST_STARTUP="CONTAINER_FIRST_STARTUP"
if [ ! -e /$CONTAINER_FIRST_STARTUP ]
then
    touch /$CONTAINER_FIRST_STARTUP
    echo "First time container starting commands"
    python manage.py migrate
    python manage.py createsuperuser --username admin --no-input
    python manage.py collectstatic --no-input --clear
else
    echo "Container restarting commands"
    echo "No commands"
fi
gunicorn config.wsgi:application --bind 0.0.0.0:8000 -p 8000