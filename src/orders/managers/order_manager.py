"""Order manager"""
from django.db import models

from src.users.models import User


class OrderManager(models.Manager):
    """Order manager."""

    def get_orders_count(self, user: User):
        """
        Get orders count for user.

        :param user: User object.
        :return: Total count of orders
        """
        return self.filter(user=user).count()

