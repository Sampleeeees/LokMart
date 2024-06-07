"""Auth schemas."""

from ninja import Schema
from pydantic import EmailStr


class LoginSchema(Schema):
    """Login schemas."""

    email: str
    password: str


class LoginResponseSchema(Schema):
    """Login response schema."""

    access_token: str
    refresh_token: str


class SuccessSchema(Schema):
    """Success message schema."""

    message: str | None


class EmailSchema(Schema):
    """Email schema."""

    email: EmailStr


class VerifyEmailSchema(Schema):
    """Verify email schema."""

    email: EmailStr
    code: int


class EmailAlreadyRegisteredSchema(Schema):
    """User with email already registered schema."""

    detail: str = "Email already registered"


class RegisterUserSchema(Schema):
    """Register new user schema."""

    full_name: str
    email: EmailStr
    password: str

    class Config:
        """Class Config for set json extra schema."""

        json_schema_extra = {
            "example": {
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "password": "strongpassword123",
            }
        }


class RegisterOutUserSchema(Schema):
    """Register successfully user schema."""

    status_code: int
    message: str
    access_token: str
    refresh_token: str
