"""Products exceptions."""

from src.core.base import HttpBaseError


class ProductNotFoundExceptionError(HttpBaseError):
    """Product not found."""

    code = "NOT_FOUND"
    message = "Product not found."
    field = ""
    location = ""
    status_code = 404
