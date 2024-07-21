"""Help exceptions module."""

from src.core.base import HttpBaseError


class WelcomeBlockNotFoundExceptionError(HttpBaseError):
    """Welcome blocks not found."""

    status_code = 404
    code = "WELCOME_NOT_FOUND"
    message = "Welcome blocks not found"
    location = ""
    field = ""


class HelpCenterNotFoundExceptionError(HttpBaseError):
    """Help center not found."""

    status_code = 404
    code = "HELP_CENTER_NOT_FOUND"
    message = "Help center not found"
    location = ""
    field = ""
