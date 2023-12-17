from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'product_category')
    list_filter = ('product_category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
