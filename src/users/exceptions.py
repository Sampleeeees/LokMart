"""User Exceptions."""

from src.core.base import HttpBaseError


class UserNotFoundExceptionError(HttpBaseError):
    """User no found exceptions."""

    code = "USER_NOT_FOUND"
    message = "User not found."
    field = ""
    location = ""
    status_code = 404


class InvalidVerificationCodeExceptionError(HttpBaseError):
    """Invalid token."""

    code = "INVALID_VERIFICATION_CODE"
    message = "Verification code is invalid."
    field = "code"
    location = ""
    status_code = 409


class VerificationCodeNotFoundExceptionError(HttpBaseError):
    """Verification code not found for this email."""

    code = "CODE_NOT_FOUND_FOR_THIS_EMAIL"
    message = "Code not found for email."
    field = "code"
    location = ""
    status_code = 404
