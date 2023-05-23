from django.contrib import admin
from .models import Product, Category, RecommendedProduct, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'friendly_name',
        'name',
    )


class RecommendedProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'recommended_product',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'comment',
        'rating',
        'added_date',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecommendedProduct, RecommendedProductAdmin)
admin.site.register(Review, ReviewAdmin)
