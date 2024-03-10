
from django.core.mail import send_mail

from celery import shared_task



"""
We can run these tasks in three ways:
- One we run them individually using the delay method e.g send_email_otp.delay()
- Or we can run them in a group using the group method e.g group(send_email_otp.s(), send_mobile_otp.s()).apply_async(). This will run the tasks in parallel
making sure that these tasks are executed simultaneously.
- Or we can run them in a chain using the chain method e.g chain(send_email_otp.s(), send_mobile_otp.s()).apply_async(). This will run the tasks in sequence
making sure that the second task is executed only after the first task is completed. This is useful when the second task depends on the first task. Meaning the second task is dependent on the first task.
"""

@shared_task(bind = True, queue='otp_worker_queue', name='send_email_otp')
def send_email_otp(self):
    mail_subject = "Here is your email OTP"
    send_mail(
        subject = mail_subject,
        message = "Here is your email OTP",
        from_email = "Here is your email OTP",
        recipient_list = ["Here is your email OTP"],
        fail_silently = False,
        )
    return "Done"

@shared_task(bind = True, queue='otp_worker_queue', name='send_mobile_otp')
def send_mobile_otp(self):
    mail_subject = "Here is your email OTP"
    send_mail(
        subject = mail_subject,
        message = "Here is your email OTP",
        from_email = "Here is your email OTP",
        recipient_list = ["Here is your email OTP"],
        fail_silently = False,
        )
    return "Done"
