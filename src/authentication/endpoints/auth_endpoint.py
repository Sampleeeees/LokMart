"""Authentication Endpoints."""

from django.http import HttpRequest
from ninja_extra import ControllerBase
from ninja_extra import api_controller
from ninja_extra import route

from src.authentication.schemas import EmailAlreadyRegisteredSchema
from src.authentication.schemas import RegisterOutUserSchema
from src.authentication.schemas import RegisterUserSchema
from src.authentication.schemas import SuccessSchema
from src.authentication.schemas import VerifyEmailSchema
from src.authentication.services.auth_service import AuthService
from src.core.base_openapi_extra import get_base_responses


@api_controller("/auth", tags=["auth"])
class AuthController(ControllerBase):
    """Auth controller for login."""

    def __init__(self, auth_service: AuthService):
        """Initialize."""
        self._auth_service = auth_service

    @route.post(
        "/registration",
        tags=["auth"],
        response=get_base_responses({200: SuccessSchema, 400: EmailAlreadyRegisteredSchema}),
    )
    def registration(self, request: HttpRequest, user: RegisterUserSchema) -> SuccessSchema:
        """Register a new user.

        Params:
          - **request**: *HttpRequest* -> Request object.
          - **email**: *RegisterUserSchema.email* -> Email which user registered. ***(str)***
          - **full_name**: *RegisterUserSchema.full_name* -> User full name. ***(str)***
          - **password**: *RegisterUserSchema.password* -> User password. ***(str)***

        Returns
        -------
          - **200**: *Success response* -> Message about sent code verification to email.
          - **400**: *Error response* -> User with registered email already exist.
          - **401**: *Error response* -> Unauthorized.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self._auth_service.user_register(user=user)

    @route.post(
        "/confirm-email",
        response=get_base_responses({200: RegisterOutUserSchema}),
        tags=["auth"],
    )
    def confirm_email(self, request: HttpRequest, verify_email: VerifyEmailSchema):
        """Verify email confirmation code.

        Params:
          - **request**: *HttpRequest* -> Request object.
          - **email**: *VerifyEmailSchema.email* -> Email which user registered. ***(str)***
          - **code**: *VerifyEmailSchema.code* -> Code verification. ***(int)***

        Returns
        -------
          - **200**: *Success response* -> Message about sent code verification to email.
          - **401**: *Error response* -> Unauthorized.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self._auth_service.verify_email(verify_email=verify_email)
