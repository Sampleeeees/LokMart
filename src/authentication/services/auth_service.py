"""
Authentication service.
"""
from ninja.errors import HttpError
from ninja_extra import status

from src.authentication.schemas import RegisterUserSchema, SuccessSchema
from src.users.models import User


class AuthService:
    """Auth service for managing authentication in the system."""

    @staticmethod
    def user_register(user: RegisterUserSchema):
        """
        Register a new user (Part 1)

        :param user: schema with user data (RegisterUserSchema)
        :return:
        """
        if User.objects.filter(email=user.email).exists():
            raise HttpError(status_code=status.HTTP_400_BAD_REQUEST, message="Email already registered")

        user: User = User.objects.create_user(email=user.email, password=user.password)
        user.save()
        # TODO : send code to user email
        return SuccessSchema(
            message="We send code to your email"
        )
