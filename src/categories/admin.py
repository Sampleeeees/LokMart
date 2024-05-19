from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import register
from unfold.admin import ModelAdmin
from unfold.decorators import display
from unfold.contrib.filters.admin import (
    RangeNumericFilter,
    SingleNumericFilter
)
from src.categories.models import Category


# Register your models here.

@register(Category)
class CategoryAdmin(ModelAdmin):
    """Category model Admin"""
    list_display = [
        "image_category",
        "name_category"
    ]

    search_fields = ["name"]
    ordering = ["id"]

    @display(description=_("Image"))
    def image_category(self, obj):
        """Render category image."""
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)

    @display(description=_("Name"), ordering="name")
    def name_category(self, obj):
        """Render category name."""
        return obj.name

