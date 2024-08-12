"""Country models."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from src.countries.managers.manager import CountryManager

# Create your models here.


class Country(models.Model):
    """Country model."""

    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to="images/country/", blank=True)
    lang_code = models.CharField(max_length=5)

    objects = CountryManager()

    class Meta:
        """Class meta for Country model."""

        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        """Country string representation."""
        return self.name
