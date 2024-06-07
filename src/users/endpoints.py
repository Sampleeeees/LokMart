"""User controller module."""

from django.http import HttpRequest
from ninja_extra import ControllerBase
from ninja_extra import api_controller
from ninja_extra import route
from ninja_jwt.authentication import JWTAuth

from src.core.base_openapi_extra import get_base_responses
from src.users.schemas import UserNotFound
from src.users.schemas import UserResponseSchema
from src.users.schemas import UserUpdateSchema
from src.users.service import UserService


@api_controller("/users", tags=["Users"])
class UserController(ControllerBase):
    """User controller class."""

    def __init__(self, user_service: UserService) -> None:
        """Initialize."""
        self.user_service = user_service

    @route.get(
        "/profile",
        response=get_base_responses({200: UserResponseSchema, 404: UserNotFound}),
        auth=JWTAuth(),
    )
    def get_profile(self, request: HttpRequest):
        """Get user personal info.

        Params:
          - **request**: request by authorization user.

        Returns
        -------
          - **200**: *Success response* -> User data.
          - **401**: *Error response* -> Unauthorized.
          - **404**: *Error response* -> User not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.user_service.get_my_profile(request.user.id)

    @route.patch(
        "/profile",
        response=get_base_responses({200: UserResponseSchema, 404: UserNotFound}),
        auth=JWTAuth(),
    )
    def update_profile(self, request: HttpRequest, user_body: UserUpdateSchema):
        """Update user info.

        Params:
          - **request**: *HttpRequest* -> Request object.
          - **full_name**: *UserUpdateSchema.full_name* -> New user full name. ***(str)***
          - **email**: *UserUpdateSchema.email* -> New user email. ***(str)***
          - **phone_number**: *UserUpdateSchema.phone_number* -> New user phone number. ***(str)***
          - **image**: *UserUpdateSchema.image* -> New user avatar. ***(str)***

        Returns
        -------
          - **200**: *Success response* -> User data.
          - **401**: *Error response* -> Unauthorized.
          - **404**: *Error response* -> User not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.user_service.update_my_profile(request.user.id, user_body)
