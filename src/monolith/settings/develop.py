from .base import *

ALLOWED_HOSTS += ['localhost', '127.0.0.1']

INSTALLED_APPS += []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = []

