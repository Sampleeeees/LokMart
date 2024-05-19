from ninja_extra import api_controller, ControllerBase, permissions, route
from ninja.security import APIKeyQuery

from src.users.schemas import UserResponseSchema, UserSchema
from src.users.service import UserService


@api_controller("/users")
class UserController(ControllerBase):
    """
    User controller class.
    """
    def __init__(self, user_service: UserService) -> None:
        """Initialize."""
        self.user_service = user_service

    @route.post("/create", response=UserResponseSchema)
    def create_user(self, user: UserSchema) -> UserResponseSchema:
        """Create user"""
        pass
