from django.contrib import admin
from .models import note

# Register your models here.
@admin.register(note)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'content','createdAt',"updatedAt")  

