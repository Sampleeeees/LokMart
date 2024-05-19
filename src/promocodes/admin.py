from unfold.admin import ModelAdmin
from django.contrib.admin import register
from unfold.decorators import display
from django.utils.translation import gettext_lazy as _
from src.promocodes.models import PromoCode, ProductPromoCode


# Register your models here.

@register(PromoCode)
class PromoCodeAdmin(ModelAdmin):
    """PromoCode admin model."""
    list_display = [
        "promo_code",
        "promo_code_uses",
        "promo_code_max_uses",
        "promo_code_discount",
        "promo_code_start_at",
        "promo_code_expires_at"
    ]

    @display(description=_("Promo code"))
    def promo_code(self, obj):
        return obj.code

    @display(description=_("Uses"))
    def promo_code_uses(self, obj):
        return obj.uses

    @display(description=_("Max uses"))
    def promo_code_max_uses(self, obj):
        return obj.max_uses

    @display(description=_("Discount"))
    def promo_code_discount(self, obj):
        return obj.discount

    @display(description=_("Start at"))
    def promo_code_start_at(self, obj):
        return obj.start_at.strftime('%H:%M %d.%m.%Y')

    @display(description=_("Expires at"))
    def promo_code_expires_at(self, obj):
        return obj.expires_at.strftime('%H:%M %d.%m.%Y')


@register(ProductPromoCode)
class ProductPromoCodeAdmin(ModelAdmin):
    """ProductPromoCode admin model"""
    pass
