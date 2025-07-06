from django.contrib import admin
from .models import contents

# Register your models here.
@admin.register(contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','author','createdAt',"updatedAt")  
    search_fields = ('title', 'content')
    list_filter = ('createdAt','title')