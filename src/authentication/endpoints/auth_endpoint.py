"""
Authentication Endpoints.
"""

from django.http import HttpRequest
from ninja_extra import api_controller, route, ControllerBase

from src.authentication.schemas import RegisterUserSchema, SuccessSchema, EmailSchema, \
    VerifyEmailSchema
from src.authentication.services.auth_service import AuthService


@api_controller('/auth', tags=["auth"])
class AuthController(ControllerBase):
    """
    Auth controller for login.
    """

    def __init__(self, auth_service: AuthService):
        """Initialize."""
        self._auth_service = auth_service

    @route.post("/registration", tags=["auth"], response=SuccessSchema)
    def registration(self, request: HttpRequest, user: RegisterUserSchema) -> SuccessSchema:
        """
        Register a new user

        :param request: HttpRequest request
        :param user: User data for registration (RegisterUserSchema)
        :return:
        """
        return self._auth_service.user_register(user=user)

    @route.post("/confirm-email", tags=["auth"])
    def confirm_email(self, request: HttpRequest, verify_email: VerifyEmailSchema):
        """
        Verify email confirmation code

        :param request: HttpRequest request
        :param verify_email: Schema with email and code
        :return: SuccessSchema | HttpError
        """
        return self._auth_service.verify_email(verify_email=verify_email)

    # @route.post("/reset-password", tags=["auth"], response=SuccessSchema)
    # def reset_password(self, request: HttpRequest, email: EmailSchema):
    #     """
    #     Reset user password
    #
    #     :param request: HttpRequest request
    #     :param email: User email (EmailSchema)
    #     :return:
    #     """
    #     return self._auth_service.reset_password(email=email)

    # @route.post("/change-password", tags=["auth"], response=SuccessSchema)
    # def change_password(self, request: HttpRequest, change_schema: ChangePasswordSchema) -> SuccessSchema:
    #     """
    #     Change user password
    #
    #     :param request: Http request
    #     :param change_schema: Schema with data for changing password
    #     :return:
    #     """
    #     return self._auth_service.change_password(change_schema)

    # @route.post("/confirm-email", tags=["auth"], response=SuccessSchema)
    # def confirm_email(self, request: HttpRequest, )