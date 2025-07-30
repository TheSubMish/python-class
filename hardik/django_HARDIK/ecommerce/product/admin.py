from django.contrib import admin
from django import forms

from .models import Product,Category,SubCategory
# Register your models here.
@admin.register(Product)
class ProductContents(admin.ModelAdmin):
    list_display=['name','price','stock','category','subcategory']
    list_filter=['category','subcategory']

@admin.register(Category)
class CategoryContents(admin.ModelAdmin):
    list_display=['name']
    search_fields = ['name']

@admin.register(SubCategory)
class SubCategoryContents(admin.ModelAdmin):
    list_display=['name','category']
    search_fields = ['name']