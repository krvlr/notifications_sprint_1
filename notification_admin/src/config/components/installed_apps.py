import os

from dotenv import load_dotenv

load_dotenv()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notification.apps.NotificationConfig',
    'corsheaders',
]

if os.environ.get('DEBUG', False) == 'True':
    INSTALLED_APPS += (
        'debug_toolbar',
    )
