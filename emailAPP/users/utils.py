from django.core.mail import send_mail
from django.conf import settings

from .models import CustomUser

def send_email():
    subject="This is test email"
    message="BE CONSISTENT AND YOU WILL REACH YOUR GOAL"
    from_email=settings.EMAIL_HOST_USER
    recipient=['isalman.ahmad01@gmail.com']
    send_mail(
        subject,
        message,
        from_email,
        recipient
    )