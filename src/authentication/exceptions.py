"""Exceptions schema."""

from django.utils.translation import gettext as _
from ninja.errors import HttpError
from ninja_extra import status


class UserEmailNotFoundError(HttpError):
    """Exception when user with given email not found."""

    def __init__(self) -> None:
        """Initialize exception."""
        self.status_code: int = status.HTTP_404_NOT_FOUND
        self.message: str = _("User with given email not found")
        super().__init__(self.status_code, self.message)


class EmailConfirmationNotFoundError(HttpError):
    """Exception when email not find for confirmed."""

    def __init__(self) -> None:
        """Initialize the error exception."""
        self.status_code: int = status.HTTP_404_NOT_FOUND
        self.message: str = _("Email not found for confirmation")
        super().__init__(self.status_code, self.message)
