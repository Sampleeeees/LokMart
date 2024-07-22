"""Helps app admin file."""

from django import forms
from django.contrib.admin import register
from django.db import models
from django.db.models import Field
from django.http import HttpRequest
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from src.helps.models import HelpCenter
from src.helps.models import PolicyPage
from src.helps.models import WelcomeBlock

# Register your models here.


@register(WelcomeBlock)
class WelcomeBlockAdmin(ModelAdmin):
    """Welcome block admin model."""

    list_display = [
        "welcome_order",
        "welcome_image",
        "welcome_text",
        "welcome_description",
    ]

    @display(description=_("Position"))
    def welcome_order(self, obj):
        """Render welcome order position."""
        return obj.order

    @display(description=_("Image"))
    def welcome_image(self, obj):
        """Return welcome image."""
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)

    @display(description=_("Text"))
    def welcome_text(self, obj):
        """Render welcome text."""
        return obj.title

    @display(description=_("Description"))
    def welcome_description(self, obj):
        """Render welcome description."""
        return obj.description

    fieldsets = (
        (
            None,
            {
                "fields": [
                    ("title", "order"),
                    "description",
                    "image",
                ],
            },
        ),
    )

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    def formfield_for_dbfield(self, db_field: Field, request: HttpRequest, **kwargs) -> Field | None:
        """Change widget for description."""
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == "description":
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


@register(HelpCenter)
class HelpCenterAdmin(ModelAdmin):
    """Help Center admin model."""

    list_display = ["help_name", "help_description"]

    @display(description=_("Question"))
    def help_name(self, obj):
        """Render help name."""
        return obj.title

    @display(description=_("Answer"))
    def help_description(self, obj):
        """Render help description."""
        return obj.description


@register(PolicyPage)
class PolicyPageAdmin(ModelAdmin):
    """Policy page admin model."""

    list_display = [
        "policy_name",
        "policy_description",
    ]

    @display(description=_("Title"))
    def policy_name(self, obj):
        """Return policy name."""
        return obj.title

    @display(description=_("Description"))
    def policy_description(self, obj):
        """Return policy description."""
        return obj.description

    def formfield_for_dbfield(self, db_field: Field, request: HttpRequest, **kwargs) -> Field | None:
        """Change widget for description."""
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == "description":
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
