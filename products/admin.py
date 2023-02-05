from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Extend the built-in ModelAdmin class. The tuple
    tells the admin which fields to display. 
    Products are ordered according to their sku 
    (must be a tuple)
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Extends the built-in ModelAdmin class. If you want to
    adjust the order in the tuple.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
