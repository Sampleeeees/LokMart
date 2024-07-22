"""Help models."""

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class WelcomeBlock(models.Model):
    """Model with welcome message."""

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images/welcome/")
    order = models.IntegerField(default=0)

    objects = models.Manager()

    class Meta:
        """Class meta for welcome model."""

        verbose_name = _("welcome block")

    def __str__(self):
        """Welcome block string representation."""
        return self.title


class HelpCenter(models.Model):
    """Help center model."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=750)

    objects = models.Manager()

    class Meta:
        """Class meta for help center."""

        verbose_name = _("help center")

    def __str__(self):
        """Help center string representation."""
        return self.title


class PolicyPage(models.Model):
    """Model for policies."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=750)

    objects = models.Manager()

    class Meta:
        """class Meta for policy page."""

        verbose_name = _("Terms & Conditions")

    def __str__(self):
        """Policy string representation."""
        return self.title
