
from accounts.models import Account

from django.core.mail import send_mail
from chat_app import settings

from celery import shared_task

@shared_task
def send_welcome_email():
    return

@shared_task(bind=True, queue='general_worker_queue')
def send_confirmation_email(self, target_mail, message):
    mail_subject = "Welcome on Board!"
    send_mail(
        subject = mail_subject,
        message = message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [target_mail],
        fail_silently = False,
        )
    return "Done"
