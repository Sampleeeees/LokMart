"""Auth schemas."""

from pydantic import EmailStr

from src.core.base_schema import BaseSchema


class LoginSchema(BaseSchema):
    """Login schemas."""

    email: str
    password: str


class LoginResponseSchema(BaseSchema):
    """Login response schema."""

    access_token: str
    refresh_token: str


class SuccessSchema(BaseSchema):
    """Success message schema."""

    message: str | None


class EmailSchema(BaseSchema):
    """Email schema."""

    email: EmailStr


class VerifyEmailSchema(BaseSchema):
    """Verify email schema."""

    email: EmailStr
    code: int


class EmailAlreadyRegisteredSchema(BaseSchema):
    """User with email already registered schema."""

    detail: str = "Email already registered"


class RegisterUserSchema(BaseSchema):
    """Register new user schema."""

    full_name: str
    email: EmailStr
    password: str


class RegisterOutUserSchema(BaseSchema):
    """Register successfully user schema."""

    status_code: int
    message: str
    access_token: str
    refresh_token: str
