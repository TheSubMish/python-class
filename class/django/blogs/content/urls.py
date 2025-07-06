from django.urls import path

from .views import blog_get_post_view, blog_detail_update_delete_view, error_page, blog_delete_view


urlpatterns = [
    path('', blog_get_post_view, name='blog_list_create'),
    path('<int:pk>/', blog_detail_update_delete_view, name='blog_detail_update_delete'),
    path('delete/<int:pk>/', blog_delete_view, name='blog_delete'),
    path('error/', error_page, name='error_page'),
]