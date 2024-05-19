"""Categories service."""
from typing import List, Union

from src.categories.models import Category


class CategoryService:
    """Category service class."""

    @staticmethod
    def get_categories() -> List[Category]:
        """
        Get all categories.

        :return: List of categories.
        """
        return Category.objects.all()

    @staticmethod
    def find_category_by_name(name: str) -> Union[List[Category], Category, None]:
        """
        Find category by name.

        :param name: Name category(str)
        :return: Category object or None
        """
        category = Category.objects.search_categories_by_name(name=name)
        if category:
            return category
        return None

