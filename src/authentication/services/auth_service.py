"""
Authentication service.
"""
import random

from ninja.errors import HttpError
from ninja_extra import status
from ninja_jwt.tokens import RefreshToken
import redis

from config import settings
from src.authentication.schemas import RegisterUserSchema, SuccessSchema, VerifyEmailSchema, LoginResponseSchema
from src.authentication.tasks import send_verification_code
from src.users.models import User

redis_instance = redis.from_url(settings.REDIS_URL)


class AuthService:
    """Auth service for managing authentication in the system."""

    @staticmethod
    def generate_access_refresh_token(user: User) -> LoginResponseSchema:
        """
        Generate access and refresh token after successfully confirmed email

        :param user: User object.
        :return: Login response schema with access token and refresh token
        """
        token: RefreshToken = RefreshToken.for_user(user)  # noqa
        return LoginResponseSchema(access_token=str(token.access_token), refresh_token=str(token))

    @staticmethod
    def generate_verification_code() -> int:
        """Generate verification 4-digit code. """
        return random.randint(1000, 9999)

    def user_register(self, user: RegisterUserSchema) -> SuccessSchema:
        """
        Register a new user (Part 1)

        :param user: schema with user data (RegisterUserSchema)
        :return:
        """
        if User.objects.filter(email=user.email).exists():
            raise HttpError(status_code=status.HTTP_400_BAD_REQUEST, message="Email already registered")

        verification_code: int = self.generate_verification_code()

        redis_instance.set(user.email, verification_code, ex=600)

        send_verification_code.delay(email=user.email, code=verification_code)
        User.objects.create_user(email=user.email, password=user.password, full_name=user.full_name, is_active=False)
        return SuccessSchema(
            message="We send code to your email"
        )

    def verify_email(self, verify_email: VerifyEmailSchema):
        """
        Verify user code and active his account

        :param verify_email: Schema with email and code
        :return: Success Schema about success registration
        """
        user: User = User.objects.filter(email=verify_email.email, is_active=False).first()
        if user:
            if redis_instance.get(verify_email.email):
                code: int = redis_instance.get(verify_email.email).decode("utf-8")
                if int(code) != verify_email.code:
                    raise HttpError(status_code=status.HTTP_400_BAD_REQUEST, message="Invalid verification code")
                else:
                    user.is_active = True
                    user.save()
                    # redis_instance.delete(verify_email.email)
                    token: LoginResponseSchema = self.generate_access_refresh_token(user)
                    return {
                        "status_code": status.HTTP_200_OK,
                        "message": "Successfully verified email",
                        "access_token": token.access_token,
                        "refresh_token": token.refresh_token
                    }
            else:
                raise HttpError(status_code=status.HTTP_400_BAD_REQUEST, message="This email is not start registration")
        return HttpError(status_code=status.HTTP_400_BAD_REQUEST, message="User with this email for confirmation his email not found")

