"""Product manager module."""

from django.db import models


class ProductManager(models.Manager):
    """Product manager class."""

    def search_product_by_name(self, name: str) -> models.QuerySet:
        """Find product by name.

        :param name: Name of the products.
        :return: List of products.
        """
        return self.filter(name__icontains=name)

    def get_products_by_category_name(self, category_name: str) -> models.QuerySet:
        """Get all products by category name.

        :param category_name: Name of category (str)
        :return: List of products
        """
        return self.filter(category__name=category_name)
