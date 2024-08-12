from django.contrib.admin import register
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from django.utils.translation import gettext_lazy as _
from src.countries.models import Country


# Register your models here.


@register(Country)
class CountryAdmin(ModelAdmin):
    """Country model admin"""
    list_display = [
        "country_name",
    ]

    @display(description=_("Flag"), ordering="name", header=True)
    def country_name(self, obj):
        """Render country name with image and lang code."""
        return obj.name, obj.lang_code, format_html('<img src="{}" style="max-height: 30px; max-width: 50px;" />', obj.flag.url)
