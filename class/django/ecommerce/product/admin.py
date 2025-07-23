from django.contrib import admin

from .models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)
    search_fields = ("name",)
    list_filter = ("category",)
    ordering = ("-created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
