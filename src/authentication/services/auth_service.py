"""Authentication service."""

from secrets import randbelow

import redis
from django.core.exceptions import ObjectDoesNotExist
from ninja_extra import status
from ninja_jwt.tokens import RefreshToken

from config import settings
from src.authentication.exceptions import EmailAlreadyExistExceptionError
from src.authentication.schemas import LoginResponseSchema
from src.authentication.schemas import RegisterOutUserSchema
from src.authentication.schemas import RegisterUserSchema
from src.authentication.schemas import SuccessSchema
from src.authentication.schemas import VerifyEmailSchema
from src.authentication.tasks import send_verification_code
from src.users.exceptions import InvalidVerificationCodeExceptionError
from src.users.exceptions import UserNotFoundExceptionError
from src.users.exceptions import VerificationCodeNotFoundExceptionError
from src.users.models import User

redis_instance = redis.from_url(settings.REDIS_URL)


class AuthService:
    """Auth service for managing authentication in the system."""

    @staticmethod
    def generate_access_refresh_token(user: User) -> LoginResponseSchema:
        """Generate access and refresh token after successfully confirmed email.

        :param user: User object.
        :return: Login response schema with access token and refresh token
        """
        token: RefreshToken = RefreshToken.for_user(user)
        return LoginResponseSchema(access_token=str(token.access_token), refresh_token=str(token))

    @staticmethod
    def generate_verification_code() -> int:
        """Generate verification 4-digit code."""
        return randbelow(9000) + 1000

    def user_register(self, user: RegisterUserSchema) -> SuccessSchema:
        """Register a new user (Part 1).

        :param user: schema with user data (RegisterUserSchema)
        :return:
        """
        if User.objects.filter(email=user.email).exists():
            raise EmailAlreadyExistExceptionError(message=f"User with email {user.emal} already exists.")

        verification_code: int = self.generate_verification_code()

        redis_instance.set(user.email, verification_code, ex=600)

        send_verification_code.delay(email=user.email, code=verification_code)
        User.objects.create_user(
            email=user.email,
            password=user.password,
            full_name=user.full_name,
            is_active=False,
        )
        return SuccessSchema(message="We send code to your email")

    def verify_email(self, verify_email: VerifyEmailSchema) -> RegisterOutUserSchema:
        """Verify user code and activate his account.

        :param verify_email: Schema with email and code
        :return: Success Schema about successful registration
        """
        try:
            user: User = User.objects.get(email=verify_email.email, is_active=False)
        except ObjectDoesNotExist as error:
            raise UserNotFoundExceptionError(
                message="User with this email is not registered or already active"
            ) from error

        verification_code = redis_instance.get(verify_email.email)
        if not verification_code:
            raise VerificationCodeNotFoundExceptionError(
                message=f"Verification code for {verify_email.email} not found. Start register again."
            )

        code = verification_code.decode("utf-8")
        if code != verify_email.code:
            raise InvalidVerificationCodeExceptionError(message=f"Code {code} is invalid.")

        user.is_active = True
        user.save()
        redis_instance.delete(verify_email.email)

        token = self.generate_access_refresh_token(user)
        return RegisterOutUserSchema(
            status_code=status.HTTP_200_OK,
            message="Successfully verified email",
            access_token=token.access_token,
            refresh_token=token.refresh_token,
        )
