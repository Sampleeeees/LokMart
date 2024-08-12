"""Django unfold module."""

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD_SETTINGS = {
    "SITE_TITLE": "LokMart",
    "SITE_HEADER": " ",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("lokmart_light.png"),
        "dark": lambda request: static("lokmart_dark.png"),
    },
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",
    "LOGIN": {
        "image": lambda request: static("sample/login-bg.jpg"),
    },
    "STYLES": [
        lambda request: static("unfold_admin/css/style.css"),
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("User"),
                        "icon": "people",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("Category"),
                        "icon": "category",
                        "link": reverse_lazy("admin:categories_category_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Gallery"),
                        "icon": "gallery_thumbnail",
                        "link": reverse_lazy("admin:gallery_gallery_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Image"),
                        "icon": "image",
                        "link": reverse_lazy("admin:gallery_image_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Welcome block"),
                        "icon": "home",
                        "link": reverse_lazy("admin:helps_welcomeblock_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Help"),
                        "icon": "help",
                        "link": reverse_lazy("admin:helps_helpcenter_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Terms & Conditions"),
                        "icon": "help",
                        "link": reverse_lazy("admin:helps_policypage_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Product"),
                        "icon": "home",
                        "link": reverse_lazy("admin:products_product_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Discount"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:products_productdiscount_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Review"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:reviews_review_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Tag"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:tags_tag_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Product Tag"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:products_producttag_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Promo code"),
                        "icon": "code",
                        "link": reverse_lazy("admin:promocodes_promocode_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],
            }
        ],
    },
}
