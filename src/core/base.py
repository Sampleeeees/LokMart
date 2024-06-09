"""Base HTTP Exception builder."""

import json

from ninja import Schema
from ninja.errors import HttpError
from pydantic import BaseModel
from pydantic import ConfigDict


class ErrorDetailFieldsSchema(Schema):
    """Error detail fields schema."""

    location: str = ""
    field: str = ""
    message: str = ""


class HttpBaseDetailErrorSchema(Schema):
    """Detail category error schema."""

    code: str
    details: list[ErrorDetailFieldsSchema]


class HttpBaseErrorSchema(Schema):
    """Error schema about category bot found."""

    status: int = 000
    error: HttpBaseDetailErrorSchema


class HttpBaseError(HttpError):
    """Category exception."""

    status_code: int
    code: str
    message: str
    field: str
    location: str

    def __init__(self, message: str | None = None) -> None:
        """Initialize exception."""
        if message is not None:
            self.message = message
        error_detail = HttpBaseDetailErrorSchema(
            code=self.code,
            details=[
                ErrorDetailFieldsSchema(
                    location=self.location,
                    field=self.field,
                    message=self.message,
                )
            ],
        )
        error = HttpBaseErrorSchema(
            status=self.status_code,
            error=error_detail,
        )
        super().__init__(status_code=error.status, message=json.dumps(error.dict()))


class SchemaFactory:
    """Schema factory for recreate from exception to schema."""

    @classmethod
    def json_extra_schema(cls, exc: type):
        """Generate example json schema for exception in OpenAPI."""
        class_name = f"CustomErrorSchema_{exc.__name__}"  # Generate unique class name

        # create new class
        return type(
            class_name, (Schema,), {"model_config": ConfigDict(json_schema_extra={"examples": [exc().message]})}
        )


class UnauthorizedExceptionError(HttpBaseError):
    """Exception raised when the user is not authenticated."""

    code = "UNAUTHORIZED"
    message = "Credentials were not provided."
    field = "API-key"
    location = "header"
    status_code = 403


class InvalidCredentialsExceptionError(HttpBaseError):
    """Exception raised when the user provides invalid credentials."""

    code = "LOGIN_BAD_CREDENTIALS"
    message = "Invalid credentials."
    field = "API-key"
    location = "header"
    status_code = 401


class ValidationExceptionError(HttpBaseError):
    """Exception for 422 http error."""

    code = "VALIDATION_ERROR"
    message = "string"
    field = "string"
    location = "string"
    status_code = 422


class OpenAPIExtra:
    """Class to generate the JSON schema for exceptions in OpenAPI."""

    base_exception = (
        UnauthorizedExceptionError,
        InvalidCredentialsExceptionError,
    )

    @staticmethod
    def generate_nested_schema_for_code(responses: dict, error_code: int):
        """Generate the nested schema for the given error code."""
        responses[error_code] = {}
        responses[error_code]["content"] = {}
        responses[error_code]["content"]["application/json"] = {}

    @classmethod
    def json_extra_schema(
        cls,
        *exceptions: type[Exception],
        auth: bool = False,
        success_responses: list[type[BaseModel]] | None = None,
    ) -> dict:
        """Generate the error and success responses for the OpenAPI docs."""
        responses: dict = {}

        if auth:
            exceptions += cls.base_exception

        # validation exception
        exceptions += (ValidationExceptionError,)

        error_codes = {exc.status_code for exc in exceptions if hasattr(exc, "status_code")}
        for error_code in error_codes:
            examples: dict[str, dict] = {}

            for exc in exceptions:
                instance = exc()
                if instance.status_code == error_code:
                    examples[instance.__class__.__name__] = {"summary": instance.code, "value": instance.message}

            cls.generate_nested_schema_for_code(responses, error_code)
            responses[error_code]["content"]["application/json"]["examples"] = examples

        if success_responses:
            success_codes = {success.status_code for success in success_responses}

            for success_code in success_codes:
                examples: dict[str, dict] = {}

                for success in success_responses:
                    instance = success()
                    if instance.status_code == success_code:
                        examples[instance.__class__.__name__] = {"summary": "Success", "value": instance.message}

                cls.generate_nested_schema_for_code(responses, success_code)
                responses[success_code]["content"]["application/json"]["examples"] = examples

        return {"responses": responses}


openapi_extra_schemas = OpenAPIExtra.json_extra_schema
