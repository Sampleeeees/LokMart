"""Admin file for users app."""

from django.contrib.admin import register
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.decorators import display

from src.users.models import User


@register(User)
class UserAdmin(ModelAdmin):
    """Unfold user admin model."""

    list_display = ["user_email", "user_full_name", "user_is_superuser"]

    @display(description=_("Email"), ordering="email")
    def user_email(self, obj) -> str:
        """Display user email."""
        return obj.email

    @display(description=_("Full name"))
    def user_full_name(self, obj) -> str:
        """Display user name."""
        return obj.full_name

    @display(description=_("Superuser"))
    def user_is_superuser(self, obj) -> bool:
        """Display user is superuser."""
        return obj.is_superuser

    # change position for fields
    fieldsets = (
        (
            _("User info"),
            {
                "fields": [
                    "full_name",
                    "password",
                    "image",
                    "is_active",
                    "is_superuser",
                    "is_staff",
                ],
            },
        ),
        (_("Additional"), {"fields": ["last_login", "groups", "user_permissions"]}),
    )
