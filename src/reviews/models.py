"""Review models."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.products.models import Product
from src.users.models import User


# Create your models here.


class Review(models.Model):
    """Review model."""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=750)
    rating = models.PositiveSmallIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        """Review string representation"""
        return self.name
