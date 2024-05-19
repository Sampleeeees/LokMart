"""
Auth schemas.
"""
from ninja import Schema, ModelSchema
from pydantic import EmailStr, validator


class LoginSchema(Schema):
    """Login schemas"""
    email: str
    password: str


class LoginResponseSchema(Schema):
    """Login response schema"""

    access_token: str
    refresh_token: str
    user: LoginSchema


class SuccessSchema(Schema):
    """ Success message schema """
    message: str | None


class EmailSchema(Schema):
    """ Email schema """
    email: EmailStr


class RegisterUserSchema(Schema):
    """
    Register new user schema
    """

    full_name: str
    email: EmailStr
    password: str

    @validator("full_name")
    def validate_full_name(cls, value):
        if len(value.split()) < 2:
            raise ValueError("User must have both name and surname")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "password": "strongpassword123"
            }
        }

