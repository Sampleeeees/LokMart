"""Product models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.categories.models import Category
from src.gallery.models import Gallery
from src.tags.models import Tag
from src.users.models import User


# Create your models here.

class ProductDiscount(models.Model):
    """Product discount model."""

    text = models.CharField(max_length=150)
    percentage = models.DecimalField(max_digits=3, decimal_places=0)
    color = models.CharField(max_length=7)

    class Meta:
        verbose_name = _("product discount")
        verbose_name_plural = _("product discounts")

    def __str__(self):
        """ Product discount string representation."""
        return self.text


class Product(models.Model):
    """Product model."""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    total_rating = models.PositiveIntegerField(default=0)

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    discount = models.ForeignKey(ProductDiscount, on_delete=models.CASCADE, related_name='discount_products')

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        """Product string representation."""
        return self.name


class ProductTag(models.Model):
    """Product tag model."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = _("product tag")
        verbose_name_plural = _("product tags")

    def __str__(self):
        """Product tag string representation"""
        return f"{self.product}/{self.tag}"


class FavoriteProduct(models.Model):
    """Favorite product model."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorite_products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_products')




