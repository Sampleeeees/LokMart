"""User schemas."""

from ninja import ModelSchema
from ninja import Schema
from pydantic import EmailStr
from pydantic import HttpUrl

from src.users.models import User


class UserSchema(ModelSchema):
    """User model schema."""

    repeat_password: str

    class Meta:
        """Class Meta."""

        model = User
        fields = ["full_name", "email", "password"]
        order = ["full_name", "email", "password", "repeat_password"]


class UserResponseSchema(ModelSchema):
    """User response model schema."""

    class Meta:
        """Class Meta."""

        model = User
        fields = ["full_name", "email", "phone_number", "image"]


class UserUpdateSchema(Schema):
    """User update schema."""

    full_name: str | None = None
    email: EmailStr | None = None
    phone_number: str | None = None
    image: HttpUrl | None = None


class UserNotFound(Schema):
    """User not found schema."""

    detail: str = "User not found."
