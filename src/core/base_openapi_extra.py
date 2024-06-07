"""Base exception in all endpoints."""

from src.core.exceptions import InternalServiceErrorSchema
from src.core.exceptions import UnauthorizedSchema


def get_base_responses(responses: dict) -> dict:
    """Responses for django-ninja.

    :param responses: Dict with additional responses

    :return: dict with all responses.
    """
    base_responses: dict = {401: UnauthorizedSchema, 500: InternalServiceErrorSchema}
    base_responses.update(responses)
    return base_responses
