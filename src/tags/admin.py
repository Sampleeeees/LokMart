from django.contrib.admin import register
from unfold.admin import ModelAdmin

from src.tags.models import Tag


# Register your models here.

@register(Tag)
class TagAdmin(ModelAdmin):
    """Tag model admin."""
    search_fields = ["name"]
    ordering = ["id"]
