"""Exceptions schema."""

from django.utils.translation import gettext as _
from ninja.errors import HttpError
from ninja_extra import status

from src.core.base import HttpBaseError


class EmailAlreadyExistExceptionError(HttpBaseError):
    """Email already registered exception."""

    code = "EMAIL_ALREADY_EXISTS"
    message = "User with this email already exists."
    field = "email"
    location = ""
    status_code = 409


class EmailConfirmationNotFoundError(HttpError):
    """Exception when email not find for confirmed."""

    def __init__(self) -> None:
        """Initialize the error exception."""
        self.status_code: int = status.HTTP_404_NOT_FOUND
        self.message: str = _("Email not found for confirmation")
        super().__init__(self.status_code, self.message)
