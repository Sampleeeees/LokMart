"""Product endpoints."""

from django.http import HttpRequest
from ninja_extra import ControllerBase
from ninja_extra import api_controller
from ninja_extra import permissions
from ninja_extra import route
from ninja_jwt.authentication import JWTAuth

from src.core.base import openapi_extra_schemas
from src.core.base_openapi_extra import get_base_responses
from src.products.exceptions import ProductNotFoundExceptionError
from src.products.schemas import ProductModelSchema
from src.products.services import ProductService


@api_controller("/products", tags=["Products"], permissions=[permissions.AllowAny])
class ProductController(ControllerBase):
    """Product controller."""

    def __init__(self, product_service: ProductService) -> None:
        """Initialize the controller."""
        self.product_service: ProductService = product_service

    @route.get(
        "/list",
        response=get_base_responses({200: list[ProductModelSchema], 404: ProductNotFoundExceptionError}, auth=True),
        openapi_extra=openapi_extra_schemas(ProductNotFoundExceptionError, auth=True),
        auth=JWTAuth(),
    )
    def list_products(self, request: HttpRequest, offset: int, limit: int = 100) -> list[ProductModelSchema]:
        """Get all products.

        Params
        -------
          - **request**: *HttpRequest* -> Request object.

        Returns
        -------
          - **200**: *Success response* -> List with categories.
          - **404**: *Error response* -> Products not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.product_service.get_product_list(request)

    @route.get(
        "/{id}",
        response=get_base_responses(
            {
                200: ProductModelSchema,
                404: ProductNotFoundExceptionError,
            },
            auth=True,
        ),
        openapi_extra=openapi_extra_schemas(ProductNotFoundExceptionError, auth=True),
        auth=JWTAuth(),
    )
    def get_product_by_id(self, request: HttpRequest, product_id: int) -> ProductModelSchema:
        """Get product by id."""
        return self.product_service.get_product_by_id(request, product_id)

    @route.get(
        "/by-category/{category_name}",
        response=get_base_responses(
            {
                200: ProductModelSchema,
                404: ProductNotFoundExceptionError,
            },
            auth=True,
        ),
        openapi_extra=openapi_extra_schemas(ProductNotFoundExceptionError, auth=True),
        auth=JWTAuth(),
    )
    def get_product_by_category(self, request: HttpRequest, category_name: str):
        """Get product by category.

        Params
        -------
          - **request**: *HttpRequest* -> Request object.
          - **category_name**: *Category name* -> Category name (str)

        Returns
        -------
          - **200**: *Success response* -> List with categories.
          - **404**: *Error response* -> Products not found.
          - **422**: *Error response* -> Unprocessable Entity.
          - **500**: *Internal server response* -> Unexpected error.

        """
        return self.product_service.get_products_by_category(request=request, category_name=category_name)
