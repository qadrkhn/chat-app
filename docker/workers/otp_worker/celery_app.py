
import os

from celery import Celery
from kombu import Exchange, Queue


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('otp_worker',
             broker='amqp://guest:guest@rabbitmq:5672//',)
app.config_from_object('settings', namespace='CELERY')

# first arg is name of the queue need to be same as the routing_key, also needs to be same in the command for this worker in docker-compose.yml
# second arg is the exchange name that is used to route the message to the queue
# third arg is the routing_key that is used to route the message to the queue
# fourth arg is the queue_arguments that is used to set the max priority of the queue
# app.conf.task_queues = [
#     Queue
#     (
#         'otp_worker_queue',
#         Exchange('otp_worker_queue'), routing_key='otp_worker_queue',
#         queue_arguments={'x-max-priority': 10}
#     ),
# ]

# app.conf.task_default_priority = 10
# app.conf.task_default_limit = 10/60
app.conf.task_acks_late = True

app.conf.imports = ('tasks',)

