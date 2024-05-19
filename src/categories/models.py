from django.db import models
from django.utils.translation import gettext_lazy as _

from src.categories.managers.manager import CategoryManager


# Create your models here.


class Category(models.Model):
    """
    Category model.
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/categories/')

    objects = CategoryManager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        """Return category name as human-readable presentation."""
        return self.name
