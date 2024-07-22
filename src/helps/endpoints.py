"""Help endpoints."""

from django.http import HttpRequest
from ninja_extra import api_controller
from ninja_extra import permissions
from ninja_extra import route

from src.core.base import openapi_extra_schemas
from src.core.base_openapi_extra import get_base_responses
from src.helps.exceptions import HelpCenterNotFoundExceptionError
from src.helps.exceptions import PolicyPageNotFoundExceptionError
from src.helps.exceptions import WelcomeBlockNotFoundExceptionError
from src.helps.schemas import HelpCenterModelSchema
from src.helps.schemas import PolicyPageModelSchema
from src.helps.schemas import WelcomeBlockModelSchema
from src.helps.services import HelpService


@api_controller("/help", tags=["Help & Welcome"], permissions=[permissions.AllowAny])
class HelpController:
    """Help Controller."""

    def __init__(self, help_service: HelpService):
        """Initialize."""
        self.help_service = help_service

    @route.get(
        "/welcome",
        response=get_base_responses({200: list[WelcomeBlockModelSchema], 404: WelcomeBlockNotFoundExceptionError}),
        openapi_extra=openapi_extra_schemas(WelcomeBlockNotFoundExceptionError),
    )
    def welcome(self, request: HttpRequest) -> list[WelcomeBlockModelSchema]:
        """Get welcome pages."""
        return self.help_service.get_welcome_screens()

    @route.get(
        "/center",
        response=get_base_responses({200: list[HelpCenterModelSchema], 404: HelpCenterNotFoundExceptionError}),
        openapi_extra=openapi_extra_schemas(HelpCenterNotFoundExceptionError),
    )
    def help_center(self, request: HttpRequest) -> list[HelpCenterModelSchema]:
        """Get help center question-answer."""
        return self.help_service.get_help_center()

    @route.get(
        "terms_and_conditions",
        response=get_base_responses({200: PolicyPageModelSchema, 404: PolicyPageNotFoundExceptionError}),
        openapi_extra=openapi_extra_schemas(PolicyPageNotFoundExceptionError),
    )
    def terms_and_conditions(self, request: HttpRequest) -> list[PolicyPageModelSchema]:
        """Get terms and conditions."""
        return self.help_service.get_terms_and_conditions()
