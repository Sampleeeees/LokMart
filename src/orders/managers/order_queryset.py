"""Order QuerySet."""

from django.db import models
from django.utils.translation import gettext_lazy as _
from src.users.models import User


class OrderStatus(models.TextChoices):
    EMPTY = ("", "")
    ON_DELIVERY = ("On delivery", _("On Delivery"))
    DELIVERED = ("Delivered", _("Delivered"))
    CANCELED = ("Canceled", _("Canceled"))


class OrderQuerySet(models.QuerySet):
    """Order queryset."""
    def get_queryset(self, user: User):
        """
        Get all orders by user.

        :param user: user object
        :return: List orders for user
        """
        return self.filter(user=user)

    def on_delivery(self, user: User):
        """
        Get all orders with status on delivery

        :param user: User object.
        :return: List of orders for user
        """
        return self.filter(user=user, status=OrderStatus.ON_DELIVERY)

    def delivered(self, user: User):
        """
        Get all orders by user

        :param user: User object
        :return: List of orders for user
        """
        return self.filter(user=user, status=OrderStatus.DELIVERED)

    def cancelled(self, user: User):
        """
        Get all orders by user.

        :param user: User object.
        :return: List of orders for user.
        """
        return self.filter(user=user, status=OrderStatus.CANCELED)