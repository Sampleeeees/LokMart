"""Product Services Module."""

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from django.http import HttpRequest

from src.products.exceptions import ProductNotFoundExceptionError
from src.products.models import FavoriteProduct
from src.products.models import Product
from src.products.schemas import ProductModelSchema
from src.users.models import User


class ProductService:
    """Product Service Class."""

    @staticmethod
    def list_products_with_favorite(products: QuerySet[Product], user: User) -> list[ProductModelSchema]:
        """Get products with favorite product."""
        product_schemas: list = []
        for product in products:
            favorite = FavoriteProduct.objects.filter(product=product, user=user).exists()

            product_schema = ProductModelSchema.from_orm(product)
            product_schema.is_favorite = favorite

            product_schemas.append(product_schema)
        return product_schemas

    def get_product_list(self, request: HttpRequest) -> list[ProductModelSchema]:
        """Get list of products."""
        products = Product.objects.all()

        if products:
            return self.list_products_with_favorite(products, request.user)

        raise ProductNotFoundExceptionError

    def get_product_by_id(self, request: HttpRequest, product_id: int) -> ProductModelSchema:
        """Get product by id."""
        try:
            return Product.objects.get(id=product_id)
        except ObjectDoesNotExist as error:
            raise ProductNotFoundExceptionError from error

    def get_products_by_category(self, request: HttpRequest, category_name: str):
        """Get list of products by category."""
        products = Product.objects.get_products_by_category_name(category_name)
        if products:
            product_schemas: list = []
            for product in products:
                favorite = FavoriteProduct.objects.filter(product=product, user=request.user).exists()

                product_schema = ProductModelSchema.from_orm(product)
                product_schema.is_favorite = favorite

                product_schemas.append(product_schema)
            return product_schemas
        raise ProductNotFoundExceptionError
