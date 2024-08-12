""" Category manager."""
from django.db import models


class CategoryManager(models.Manager):
    """ Category manager."""

    def search_categories_by_name(self, name: str):
        """
        Find category by name.

        :param name: Name of the category.
        :return: List of categories
        """
        return self.filter(name__icontains=name)

