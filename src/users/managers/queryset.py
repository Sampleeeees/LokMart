""" User custom QuerySet"""
from django.db import models


class UserQuerySet(models.QuerySet):
    """
    Redefined QuerySet to user
    """
    def active(self):
        """
        Get all active users

        :return: List of active users
        """
        return self.filter(is_active=True)