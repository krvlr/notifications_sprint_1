import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE',
                            default='django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', default='db_name'),
        'USER': os.getenv('DB_USER', default='db_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', default='db_password'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', 5432),
        'OPTIONS': {
            'options': '-c search_path=public,notification',
        },
    },
}
