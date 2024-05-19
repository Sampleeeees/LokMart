"""
Authentication celery tasks.
"""
from celery import shared_task


@shared_task
def send_verification_code(email, code):
    """
    Send verification code to email

    :param email: User email
    :param code: Code for verification
    :return:
    """
    #TODO: Send text and connect SMTP
    pass