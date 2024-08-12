"""Country service"""
from typing import List

from src.countries.models import Country


class CountryService:
    """ Country service class."""

    @staticmethod
    def get_all_countries() -> List[Country]:
        """
        Get all countries.

        :return: List of countries.
        """
        return Country.objects.get_all_countries()