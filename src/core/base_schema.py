"""Base django ninja schema."""

from humps.main import camelize
from ninja import Schema


class BaseSchema(Schema):
    """Custom base schema for project."""

    class Config:
        """Pydantic configuration for OpenAPI."""

        from_attributes = True
        alias_generator = camelize
        populate_by_name = True
        str_strip_whitespace = True
