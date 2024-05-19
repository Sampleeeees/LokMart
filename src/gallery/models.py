"""Gallery models."""
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Gallery(models.Model):
    """Gallery model."""
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _("gallery")

    def __str__(self):
        """Gallery string representation."""
        return self.text


class Image(models.Model):
    """Image model."""
    image = models.ImageField(upload_to='images/gallery/')

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")

