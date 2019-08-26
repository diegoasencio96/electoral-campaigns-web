from .base import *

ALLOWED_HOSTS += ['localhost', '127.0.0.1', '68.183.62.143']

INSTALLED_APPS += []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'campaigns_db',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'db',
        'PORT': '5432',
    }
}


AUTH_PASSWORD_VALIDATORS = []

