
from django.conf import settings

# TODO: COMPLETE THIS FUNCTION TO ALLOW DUAL BROKER CONFIGURATION
def execute_task(task_name, *args, **kwargs):
    if task_name in [settings.INSTALLED_APPS.tasks]:
        task = settings.INSTALLED_APPS.tasks[task_name]
    task.delay(*args, **kwargs)
