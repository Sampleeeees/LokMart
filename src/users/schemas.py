"""User schemas."""

from humps import camelize
from ninja import ModelSchema
from ninja import Schema
from pydantic import EmailStr
from pydantic import HttpUrl

from src.core.base_schema import BaseSchema
from src.users.models import User


class UserSchema(BaseSchema):
    """User model schema."""

    repeat_password: str

    class Meta:
        """Class Meta."""

        model = User
        fields = ["full_name", "email", "password"]


class UserResponseSchema(ModelSchema):
    """User response model schema."""

    class Config:
        """Class Meta."""

        model = User
        model_fields = ["full_name", "email", "phone_number", "image"]
        alias_generator = camelize
        populate_by_name = True


class UserUpdateSchema(Schema):
    """User update schema."""

    full_name: str | None = None
    email: EmailStr | None = None
    phone_number: str | None = None
    image: HttpUrl | None = None


class UserNotFound(Schema):
    """User not found schema."""

    detail: str = "User not found."
