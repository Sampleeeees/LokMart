"""Tags model"""
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Tag(models.Model):
    """Tag model."""

    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        """Tag string representation."""
        return self.name
