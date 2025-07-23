from django.contrib import admin

# Register your models here.
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "quantity", "price", "created_at", "updated_at")
    search_fields = ("product__name", "user__username")
    list_filter = ("created_at", "updated_at")
