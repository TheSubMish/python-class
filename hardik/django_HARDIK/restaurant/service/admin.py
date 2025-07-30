from django.contrib import admin
from .models import Restaurant,Menu

# Register your models here.
@admin.register(Restaurant)
class RestaurantContents(admin.ModelAdmin):
    list_display = ['name','location']
    list_filter = ['location',]
    search_fields = ['name']

@admin.register(Menu)
class MenuContents(admin.ModelAdmin):
    list_display = ['restaurant','item_name','price']
    list_filter = ['restaurant', 'item_name', 'price']
    search_fields = ['restaurant','item_name'],