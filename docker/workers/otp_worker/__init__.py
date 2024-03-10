
from docker.workers.otp_worker.celery_app import app as otp_worker_app

import os
os.environ['CELERY_CONFIG_MODULE'] = 'celery_config'

__all__ = ('otp_worker_app',)
