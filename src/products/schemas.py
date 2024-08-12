"""Product schema."""

from ninja import ModelSchema

from src.categories.schemas import CategorySchema
from src.core.base_schema import BaseSchema
from src.products.models import Product
from src.products.models import ProductDiscount


class DiscountSchema(ModelSchema):
    """Discount schema."""

    class Meta:
        """Class meta for discount schema."""

        model = ProductDiscount
        fields = "__all__"


class ProductModelSchema(ModelSchema):
    """Product schema."""

    discount: DiscountSchema
    category: CategorySchema
    is_favorite: bool = False

    class Config(BaseSchema.Config):
        """Config class for product model schema."""

        model = Product
        model_fields = "__all__"
