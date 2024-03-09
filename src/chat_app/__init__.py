
from chat_app.celery import app as celery_app

"""
Below line tells django to use the celery app we created in the celery.py file as the default celery app for our django application. This is important because it allows us to use the django-celery integration features. For example, the @shared_task decorator and some_task.delay(). Without this line, we would have to use the celery app directly to create tasks and run them which is not recommmended.
"""
__all__ = ('celery_app',)
