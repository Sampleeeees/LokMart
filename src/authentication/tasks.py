"""
Authentication celery tasks.
"""
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_verification_code(email: str, code: int) -> None:
    """
    Send verification code to email

    :param email: User email
    :param code: Code for verification

    :return: None
    """
    send_mail(
        subject="Verification Code",
        message=f"Your verification code is: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
