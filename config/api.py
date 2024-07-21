"""Django ninja api."""

import json

from ninja.errors import HttpError
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI

from src.authentication.endpoints.auth_endpoint import AuthController
from src.authentication.endpoints.token_endpoints import CustomTokenObtainPairController
from src.categories.endpoints import CategoryController
from src.helps.endpoints import HelpController
from src.products.endpoints import ProductController
from src.users.endpoints import UserController

api = NinjaExtraAPI(
    title="LokMart API",
    description="API for mobile application LokMart",
)


@api.exception_handler(HttpError)
def generic_exception_handler(request, exc: HttpError):
    """Generate custom error response."""
    try:
        error_dict = json.loads(str(exc))
    except json.JSONDecodeError:
        # Handle cases where the message is not a valid JSON string
        error_dict = {"detail": str(exc)}  # Fallback to plain string
    return api.create_response(request, error_dict, status=exc.status_code)


@api.exception_handler(ValidationError)
def validation_error_handler(request, exc: ValidationError):
    """Validate error handler."""
    error_details = []
    for error in exc.errors:
        location = ".".join(map(str, error.get("loc", [])))
        field = error.get("loc", [-1])[-1]
        message = error.get("msg", "")

        error_details.append({"location": location, "field": field, "message": message})

    return api.create_response(
        request, {"status": 422, "error": {"code": "VALIDATION_ERROR", "details": error_details}}, status=422
    )


api.register_controllers(
    AuthController,
    CustomTokenObtainPairController,
    UserController,
    CategoryController,
    ProductController,
    HelpController,
)
