from django.contrib.admin import register
from unfold.admin import ModelAdmin

from src.transactions.models import Transaction


# Register your models here.


@register(Transaction)
class TransactionAdmin(ModelAdmin):
    """Transaction model admin."""
    pass
