"""
User schemas
"""
from ninja import ModelSchema

from src.users.models import User


class UserSchema(ModelSchema):
    repeat_password: str

    class Meta:
        model = User
        fields = ["full_name", "email", "password"]
        order = ["full_name", "email", "password", "repeat_password"]


class UserResponseSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "full_name", "email", "image"]

