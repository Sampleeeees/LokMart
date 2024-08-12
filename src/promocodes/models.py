"""PromoCodes models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.products.models import Product
from src.users.models import User


# Create your models here.


class PromoCode(models.Model):
    """PromoCode model."""

    code = models.CharField(max_length=15)
    uses = models.PositiveIntegerField(default=0)
    max_uses = models.PositiveIntegerField(default=0)
    max_uses_user = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)

    start_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = _("promo code")
        verbose_name_plural = _("promo codes")

    def __str__(self):
        """PromoCode string representation."""
        return self.code


class ProductPromoCode(models.Model):
    """ProductPromoCode model."""

    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE, related_name="product_promo_codes")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="promo_codes")

    class Meta:
        verbose_name = _("product promo code")
        verbose_name_plural = _("product promo codes")

    def __str__(self):
        """Product promo code string representation."""
        return f"{self.promo_code}/{self.product}"


class UserUsesPromoCode(models.Model):
    """UserUsesPromoCode model."""

    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE, related_name="promo_codes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_promo_codes")

    class Meta:
        verbose_name = _("user uses promo code")
        verbose_name_plural = _("user uses promo codes")

    def __str__(self):
        """ User uses promo code string representation"""
        return f"{self.promo_code}/{self.user}"
