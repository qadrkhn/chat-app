
import os

# CELERY SETTINGS
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
CELERY_ACCEPT_CONTENT = {'application/json'}
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_PORT = '2525'

# RABBMITMQ SETTINGS
BROKER_HEARTBEAT = 10
BROKER_HEARTBEAT_CHECKRATE = 2.0

# Setting BROKER_POOL_LIMIT to None disables pooling
# Disabling pooling causes open/close connections for every task.
# However, the rabbitMQ cluster being behind an Elastic Load Balancer,
# the pooling is not working correctly,
# and the connection is lost at some point.
# There seems no other way around it for the time being.
BROKER_POOL_LIMIT = 0

BROKER_TRANSPORT_OPTIONS = {'confirm_publish': True}

BROKER_CONNECTION_TIMEOUT = 20
BROKER_CONNECTION_RETRY = True
BROKER_CONNECTION_MAX_RETRIES = 100
