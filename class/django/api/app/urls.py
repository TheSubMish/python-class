from django.urls import path
from .views import todo_list, simple_api, serializer_api_example, todo_detail


urlpatterns = [
    path('', simple_api, name='simple_api'),
    path('todos/', todo_list, name='todo_list'),
    path('serializer/', serializer_api_example, name='serializer_api_example'),
    path('todos/<int:pk>/', todo_detail, name='todo_detail'),
]