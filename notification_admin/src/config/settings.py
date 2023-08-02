import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    'components/allowed_hosts.py',
    'components/auth_password.py',
    'components/database.py',
    'components/installed_apps.py',
    'components/internal_ips.py',
    'components/logging.py',
    'components/middleware.py',
    'components/templates.py',
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', default=1)

DEBUG = os.environ.get('DEBUG', False) == 'True'

CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:8080", "http://127.0.0.1:80", "http://127.0.0.1:8000"]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
