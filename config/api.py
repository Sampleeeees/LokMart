"""Django ninja api."""

from ninja_extra import NinjaExtraAPI

from src.authentication.endpoints.auth_endpoint import AuthController
from src.authentication.endpoints.token_endpoints import CustomTokenObtainPairController
from src.users.endpoints import UserController

api = NinjaExtraAPI(
    title="LokMart API",
    description="API for mobile application LokMart",
)

api.register_controllers(
    AuthController,
    CustomTokenObtainPairController,
    UserController,
)
