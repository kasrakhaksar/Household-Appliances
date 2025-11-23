from django.contrib.admin import TabularInline , ModelAdmin , register
from product.models import Product, ProductImage

class ProductImageInline(TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text']
    readonly_fields = []

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'stock', 'is_active', 'created_at']
    search_fields = ['name', 'brand', 'category']
    list_filter = ['category', 'is_active', 'brand']
    inlines = [ProductImageInline]
