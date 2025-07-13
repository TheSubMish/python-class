from django.urls import path

# from .views import blog_get_post_view, blog_detail_update_delete_view, error_page, blog_delete_view

from .views import (
    author_create_view,
    blog_create_view,
    comment_create_view,
    error_page,
    blog_get_post_view,
    blog_detail_update_delete_view,
    blog_delete_view,
    create_user,
    login_view,
    logout_view,
    create_user_api_view,
    # api_view,
)


urlpatterns = [
    path("user/create/", create_user, name="user_create"),
    path("author/create/", author_create_view, name="author_create"),
    path("create/", blog_create_view, name="blog_create"),
    path("comment/create/<int:blog_id>/", comment_create_view, name="comment_create"),
    path("", blog_get_post_view, name="blog_list_create"),
    path("error/", error_page, name="error_page"),
    path("<int:pk>/", blog_detail_update_delete_view, name="blog_detail_update_delete"),
    path("delete/<int:pk>/", blog_delete_view, name="blog_delete"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("create/user/api",create_user_api_view,name="create-user-api")
    # path("api", api_view, name="api-view"),
]
