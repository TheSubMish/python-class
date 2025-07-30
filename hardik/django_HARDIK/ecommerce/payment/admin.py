from django.contrib import admin

from .models import Payment,Invoice,InvoiceItem
# Register your models here.

@admin.register(Payment)
class paymentContents(admin.ModelAdmin):
    list_display=['total_amount','status']

@admin.register(Invoice)
class InvoiceContents(admin.ModelAdmin):
    list_display=['total_amount','status']

@admin.register(InvoiceItem)
class InvoiceItemContents(admin.ModelAdmin):
    list_display=['product','total_amount']