"""Category schemas."""

from ninja import Schema


class CategoryNotFoundErrorSchema(Schema):
    """Category not found error schema."""

    detail: str = "YES"


class CategorySchema(Schema):
    """Detail schema for category."""

    id: int
    name: str
    image: str
