from typing import Optional

from django import forms
from django.contrib.admin import register
from django.db.models import Field
from django.http import HttpRequest
from unfold.admin import ModelAdmin

from src.reviews.models import Review


# Register your models here.

@register(Review)
class ReviewAdmin(ModelAdmin):
    """Review model admin."""

    fieldsets = (
        (
            None,
            {
                "fields": [
                    ("name", "rating"),
                    "description",
                    # "rating",
                    ("user", "product")
                ]
            }
        ),
    )

    def formfield_for_dbfield(
        self, db_field: Field, request: HttpRequest, **kwargs
    ) -> Optional[Field]:
        formfield = super(ReviewAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == "description":
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
