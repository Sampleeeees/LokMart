"""Django ninja api."""

import json

from ninja.errors import HttpError
from ninja_extra import NinjaExtraAPI

from src.authentication.endpoints.auth_endpoint import AuthController
from src.authentication.endpoints.token_endpoints import CustomTokenObtainPairController
from src.categories.endpoints import CategoryController
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


api.register_controllers(
    AuthController,
    CustomTokenObtainPairController,
    UserController,
    CategoryController,
)
