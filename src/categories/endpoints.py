"""Category endpoints."""
from ninja.security import APIKeyQuery
from ninja_extra import ControllerBase, api_controller, route, permissions


@api_controller("/categories", auth=[APIKeyQuery()], permissions=[permissions.IsAuthenticated])
class CategoryController(ControllerBase):
    """Category endpoints."""
    pass
