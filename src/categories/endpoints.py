"""Category endpoints."""

from django.http import HttpRequest
from ninja_extra import ControllerBase
from ninja_extra import api_controller
from ninja_extra import permissions
from ninja_extra import route

from src.categories.exceptions import CategoryListNotFoundExceptionError
from src.categories.exceptions import CategoryNotFoundByIdExceptionError
from src.categories.exceptions import CategoryNotFoundExceptionError
from src.categories.schemas import CategoryNotFoundErrorSchema
from src.categories.schemas import CategorySchema
from src.categories.services import CategoryService
from src.core.base import openapi_extra_schemas
from src.core.base_openapi_extra import get_base_responses


@api_controller("/categories", tags=["Category"], permissions=[permissions.AllowAny])
class CategoryController(ControllerBase):
    """Category endpoints."""

    def __init__(self, category_service: CategoryService) -> None:
        """Initialize.

        :param category_service: Category service.
        """
        self.category_service: CategoryService = category_service

    @route.get(
        "/",
        response=get_base_responses({200: list[CategorySchema], 404: CategoryListNotFoundExceptionError}),
        openapi_extra=openapi_extra_schemas(CategoryListNotFoundExceptionError),
    )
    def list_categories(self, request: HttpRequest) -> list[CategorySchema]:
        """Get all categories.

        Params
        -------
          - **request**: *HttpRequest* -> Request object.

        Returns
        -------
          - **200**: *Success response* -> List with categories.
          - **404**: *Error response* -> Categories not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.category_service.get_categories(request=request)

    @route.get(
        "/{name}",
        response=get_base_responses(
            {
                200: list[CategorySchema],
                404: CategoryNotFoundExceptionError,
            }
        ),
        openapi_extra=openapi_extra_schemas(CategoryNotFoundExceptionError),
    )
    def get_categories_by_name(self, request: HttpRequest, name: str):
        """Get categories by name.

        Params
        -------
          - **request**: *HttpRequest* -> Request object.
          - **name**: -> Category name. ***(str)***

        Returns
        -------
          - **200**: *Success response* -> List with categories.
          - **404**: *Error response* -> Category not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.category_service.find_category_by_name(request=request, name=name)

    @route.get(
        "category/{category_id}",
        response=get_base_responses({200: CategorySchema, 404: CategoryNotFoundByIdExceptionError}),
        openapi_extra=openapi_extra_schemas(CategoryNotFoundByIdExceptionError),
    )
    def get_category_by_id(
        self, request: HttpRequest, category_id: int
    ) -> CategorySchema | CategoryNotFoundErrorSchema:
        """Get category by id.

        Params
        -------
          - **request**: *HttpRequest* -> Request object.
          - **id**: -> Category id. ***(int)***

        Returns
        -------
          - **200**: *Success response* -> List with categories.
          - **404**: *Error response* -> Category not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.category_service.get_category_by_id(request=request, category_id=category_id)
