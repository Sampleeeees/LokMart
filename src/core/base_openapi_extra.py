"""Base exception in all endpoints."""

from src.core.base import InvalidCredentialsExceptionError
from src.core.base import SchemaFactory
from src.core.base import UnauthorizedExceptionError
from src.core.base import ValidationExceptionError


def get_base_responses(responses: dict, *, auth: bool = False) -> dict:
    """Responses for django-ninja.

    :param responses: Dict with additional responses
    :param auth: User for default responses

    :return: dict with all responses.
    """
    base_responses: dict = {}
    if auth:
        base_responses: dict = {
            401: SchemaFactory.json_extra_schema(InvalidCredentialsExceptionError),
            403: SchemaFactory.json_extra_schema(UnauthorizedExceptionError),
        }

    # validation error
    base_responses[422] = SchemaFactory.json_extra_schema(ValidationExceptionError)

    for response_type, response_value in responses.items():
        if "Exception" in response_value.__name__:
            # If the response_value is a subclass of Exception, generate a custom error schema
            base_responses[response_type] = SchemaFactory.json_extra_schema(response_value)
        else:
            # Otherwise, use the response_value as-is
            base_responses[response_type] = response_value

    return base_responses
