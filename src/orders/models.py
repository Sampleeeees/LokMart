"""Order models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.orders.managers.order_manager import OrderManager
from src.orders.managers.order_queryset import OrderQuerySet, OrderStatus
from src.products.models import Product
from src.users.models import User, Address


# Create your models here.

class Order(models.Model):
    """Order model."""
    order_status = models.CharField(choices=OrderStatus.choices, default=OrderStatus.EMPTY)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField()
    on_delivery_at = models.DateTimeField()
    delivered_at = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address_orders")

    objects = OrderManager.from_queryset(OrderQuerySet)()

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        """Order string representation."""
        return f"Order_for_{self.user}"


class OrderProduct(models.Model):
    """ Order product model."""

    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_products")

    @property
    def product_total_cost(self):
        """Calculate the total price for this order product."""
        return self.quantity * self.unit_price

    def __str__(self):
        """Order product string representation"""
        return f"Order product from {self.order}"


