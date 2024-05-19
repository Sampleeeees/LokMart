"""Country manager."""

from django.db import models


class CountryManager(models.Manager):
    """Country manager class."""

    def get_all_countries(self):
        """
        Get all countries

        :return: List of countries
        """
        return self.all()

