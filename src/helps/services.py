"""Helps service module."""

from src.helps.exceptions import HelpCenterNotFoundExceptionError
from src.helps.exceptions import WelcomeBlockNotFoundExceptionError
from src.helps.models import HelpCenter
from src.helps.models import WelcomeBlock
from src.helps.schemas import HelpCenterModelSchema
from src.helps.schemas import WelcomeBlockModelSchema


class HelpService:
    """Help service class."""

    @staticmethod
    def get_welcome_screens() -> list[WelcomeBlockModelSchema]:
        """Get welcome screens."""
        if welcome := WelcomeBlock.objects.all():
            return welcome
        raise WelcomeBlockNotFoundExceptionError

    @staticmethod
    def get_help_center() -> list[HelpCenterModelSchema]:
        """Get help center question-answer."""
        if help_center := HelpCenter.objects.all():
            return help_center
        raise HelpCenterNotFoundExceptionError
