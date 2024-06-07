"""Exceptions."""

from ninja import Schema


class UnauthorizedSchema(Schema):
    """Unauthorized schema."""

    detail: str = "Unauthorized"


class InternalServiceErrorSchema(Schema):
    """Internal server error schema."""

    detail: str = "Internal server error"
