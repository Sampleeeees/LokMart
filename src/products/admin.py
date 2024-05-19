from typing import Optional

from django import forms
from django.contrib.admin import register
from django.db.models import DecimalField, Field
from django.http import HttpRequest
from unfold.admin import ModelAdmin, display
from django.utils.translation import gettext_lazy as _
from src.products.models import Product, ProductDiscount, ProductTag


# Register your models here.


@register(Product)
class ProductAdmin(ModelAdmin):
    """Product model admin."""
    list_display = [
        "product_name",
        "product_price",
        "product_stock_quantity",
        "product_total_rating",
        "product_category",
        "product_discount",
        "product_gallery",
        "product_description",
    ]

    search_fields = ["name"]
    ordering = ["price"]

    autocomplete_fields = [
        "gallery",
        "category",
        "discount"
    ]

    @display(description=_("Name"), ordering="name")
    def product_name(self, obj: Product) -> str:
        """Display product name."""
        return obj.name

    @display(description=_("Price"), ordering="price")
    def product_price(self, obj: Product) -> DecimalField:
        """Display product price."""
        return obj.price

    @display(description=_("Stock quantity"), ordering="stock_quantity")
    def product_stock_quantity(self, obj: Product) -> int:
        """Display product stock quantity"""
        return obj.stock_quantity

    @display(description=_("Rating"), ordering="total_rating")
    def product_total_rating(self, obj: Product) -> int:
        """Display total product rating"""
        return obj.total_rating

    @display(description=_("Category"))
    def product_category(self, obj: Product) -> str:
        """Display product category name"""
        return obj.category.name

    @display(description=_("Discount"))
    def product_discount(self, obj: Product) -> DecimalField:
        """Display product discount percentage"""
        return obj.discount.percentage

    @display(description=_("Count images"))
    def product_gallery(self, obj: Product) -> int:
        """Display count of images in product gallery"""
        if obj.gallery:
            return obj.gallery.images.count()
        return obj.gallery

    @display(description=_("Description"))
    def product_description(self, obj: Product) -> str:
        """Display product description"""
        return obj.description

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                    "description",
                    ("price", "stock_quantity", "total_rating"),
                    "category",
                    ("discount", "gallery")
                ]
            }
        ),
    )

    def formfield_for_dbfield(
            self,
            db_field: Field,
            request: HttpRequest,
            **kwargs
    ) -> Optional[Field]:
        """ Change widget for description"""
        formfield = super(ProductAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == "description":
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


@register(ProductDiscount)
class ProductDiscountAdmin(ModelAdmin):
    """Product discount model admin."""

    search_fields = ["text", "percentage"]
    ordering = ["id"]


@register(ProductTag)
class ProductTagAdmin(ModelAdmin):
    """Product tag model admin."""
    list_display = [
        "product_name",
        "tag_name"
    ]

    autocomplete_fields = ["product", "tag"]
    search_fields = ["product", "tag"]
    ordering = ["id"]

    @display(description=_("Product name"), )
    def product_name(self, obj: ProductTag) -> str:
        """Render product name"""
        return obj.product.name

    @display(description=_("Tag name"))
    def tag_name(self, obj: ProductTag) -> str:
        """Render tag name"""
        return obj.tag.name
