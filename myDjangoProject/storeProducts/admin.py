from django.contrib import admin

from .models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category',)
    # readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)

