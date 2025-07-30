from django.contrib import admin
from .models import contents,Author

# Register your models here.
@admin.register(contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','createdAt',"updatedAt")  
    search_fields = ('title', 'content')
    list_filter = ('createdAt','title')

@admin.register(Author)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('name','email')  
    search_fields = ('name','email')