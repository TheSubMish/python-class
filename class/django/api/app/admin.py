from django.contrib import admin

# Register your models here.
from .models import TodoModel

@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title",)
    ordering = ("-created_at",)
    date_hierarchy = "created_at"