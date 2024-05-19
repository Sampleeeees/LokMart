from django.utils.translation import gettext_lazy as _
from django.contrib.admin import register
from unfold.admin import ModelAdmin
from unfold.decorators import display
from src.gallery.models import Image, Gallery


# Register your models here.


@register(Image)
class ImageAdmin(ModelAdmin):
    """Image model admin"""
    list_display = [
        "image_name"
    ]

    autocomplete_fields = ["gallery"]

    @display(description=_("Image name"))
    def image_name(self, obj):
        return f"Image({obj.id})"


@register(Gallery)
class GalleryAdmin(ModelAdmin):
    """Gallery admin model"""
    search_fields = ["text"]
    ordering = ["id"]

    list_display = [
        "gallery_name",
        "related_images"
    ]

    @display(description=_("Count images"))
    def related_images(self, obj):
        """Count all images in gallery"""
        return obj.images.count()

    @display(description=_("Name"))
    def gallery_name(self, obj):
        """Render gallery name"""
        return obj.text
