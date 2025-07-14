from django.urls import path
from .views import todo_list, simple_api


urlpatterns = [
    path('', simple_api, name='simple_api'),
    path('todos/', todo_list, name='todo_list'),
]