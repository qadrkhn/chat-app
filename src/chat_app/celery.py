
import os

from celery import Celery


"""
When we run python manage.py runserver, the line os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings') sets the DJANGO_SETTINGS_MODULE environment variable to chat_app.settings. This is the settings file that Django will use to configure the application.
As for our celery worker, we are not running it using the manage.py command. We are running it using the celery command. This means that we need to set the DJANGO_SETTINGS_MODULE environment variable manually. So that our celery worker knows which settings file to use and has access to the configurations in the settings.py file.
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

# Create a new instance of the Celery class
app = Celery('chat_app')

"""
The below line tells the celery app to use the default Django settings file and look for the CELERY namespace in the settings file. This is where we will configure the celery app. So anythings that starts with CELERY_ in the settings file will be used to configure the celery app (example CELERY_BROKER_URL) etc.
"""
app.config_from_object('django.conf:settings', namespace='CELERY')

"""
The below line will tell celery to auto discover tasks in all the installed apps. This means that we can create a tasks.py file in any of our installed apps and celery will automatically discover the tasks in the file.
"""
app.autodiscover_tasks()
