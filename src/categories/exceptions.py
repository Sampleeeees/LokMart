"""Category exceptions."""

from src.core.base import HttpBaseError


class CategoryListNotFoundExceptionError(HttpBaseError):
    """Not found category in db."""

    code = "NOT_FOUND"
    message = "No category was created"
    field = ""
    location = ""
    status_code = 404


class CategoryNotFoundExceptionError(HttpBaseError):
    """Not found category exception."""

    code = "NOT_FOUND_BY_NAME"
    message = "The category not found by this name"
    field = "name"
    location = ""
    status_code = 404


class CategoryNotFoundByIdExceptionError(HttpBaseError):
    """Not found category by id."""

    code = "NOT_FOUND_BY_ID"
    message = "The category not found by this id."
    field = "id"
    location = ""
    status_code = 404
