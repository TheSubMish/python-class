from django.contrib import admin
from .models import Cart,OrderItem,Order
# Register your models here.
@admin.register(Cart)
class CartContents(admin.ModelAdmin):
    list_display=['user','product','quantity','price']

@admin.register(Order)
class OrderContents(admin.ModelAdmin):
    list_display=['user','status','customer_details']

@admin.register(OrderItem)
class OrderItemContents(admin.ModelAdmin):
    list_display=['product','quantity','total_amount']