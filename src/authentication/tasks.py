"""Authentication celery tasks."""

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from src.users.models import User


@shared_task
def send_verification_code(email: str, code: int) -> None:
    """Send verification code to email.

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


@shared_task
def send_reset_password(email: str, password: str) -> None:
    """Send reset password to user email.

    :param email: User email.
    :param password: New user password

    :return: None
    """
    send_mail(
        subject="Reset Password",
        message=f"Your password is: {password}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


@shared_task
def check_non_active_user(user_id: int) -> None:
    """Check if user is not active then delete him.

    :param user_id: User id in system(int)
    :return: None
    """
    try:
        user: User = User.objects.get(pk=user_id)
        if not user.is_active:
            user.delete()
    except User.DoesNotExist:
        pass
