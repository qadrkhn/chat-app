
from accounts.models import Account

from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task

"""
We can run these tasks in three ways:
- One we run them individually using the delay method e.g send_email_otp.delay()
- Or we can run them in a group using the group method e.g group(send_email_otp.s(), send_mobile_otp.s()).apply_async(). This will run the tasks in parallel
making sure that these tasks are executed simultaneously.
- Or we can run them in a chain using the chain method e.g chain(send_email_otp.s(), send_mobile_otp.s()).apply_async(). This will run the tasks in sequence
making sure that the second task is executed only after the first task is completed. This is useful when the second task depends on the first task. Meaning the second task is dependent on the first task.
"""

@shared_task(bind=True, queue='general_worker_queue')
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
