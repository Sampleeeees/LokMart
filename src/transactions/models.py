"""Transactions models."""
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class TransactionChoice(models.TextChoices):
    """Transaction choices."""
    SUCCESS = "Success", _("Success")
    ERROR = "Error", _("Error")
    FAILURE = "Failure", _("Failure")


class PaymentMethodChoice(models.TextChoices):
    """Payment method choices."""
    CASH = "CASH", _("Cash")
    CARD = "CARD", _("Card")


class Transaction(models.Model):
    """Transaction model."""

    external_id = models.CharField(max_length=100, unique=True)
    private_key = models.CharField(max_length=256)
    public_key = models.CharField(max_length=256)
    status = models.CharField(choices=TransactionChoice.choices)
    payment_method = models.CharField(choices=PaymentMethodChoice.choices, default=PaymentMethodChoice.CARD)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")

    def __str__(self):
        """Transaction string representation."""
        return self.external_id
    