
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
app = Celery('otp_worker')

app.config_from_object('celery_config', namespace='CELERY')
app.conf.imports = ('otp_tasks',)

