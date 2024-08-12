from django.contrib.admin import register
from unfold.admin import ModelAdmin

from src.orders.models import Order


# Register your models here.

@register(Order)
class OrderAdmin(ModelAdmin):
    """Order model admin."""
    pass
