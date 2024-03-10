
from django.core.mail import send_mail

from celery import shared_task


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
