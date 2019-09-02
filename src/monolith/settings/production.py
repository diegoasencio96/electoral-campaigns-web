from .base import *

from celery.schedules import crontab

ALLOWED_HOSTS += ['localhost', '127.0.0.1', '68.183.62.143', 'campaigns.diegoasencio.co']

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


IMPORT_EXPORT_USE_TRANSACTIONS = True


CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

'''
CELERY_BEAT_SCHEDULE = {
    'resetear_monto_maximo_diario_task': {
        'task': 'apps.usuarios.tasks.resetear_monto_maximo_diario',
        'schedule': crontab('0', '0', '*', '*', '*')  # “At 12:00.”
    },
    'realizar_cobro_mensualidad_task': {
        'task': 'apps.facturacion.tasks.realizar_cobro_mensualidad',
        'schedule': crontab('0', '0', '1', '*', '*')
    }
}
'''