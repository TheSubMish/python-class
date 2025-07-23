from django.urls import path
from .views import CategoryViewSet, ProductViewSet


urlpatterns = [
    path(
        "categories/",
        CategoryViewSet.as_view({"get": "list", "post": "create"}),
        name="category-list",
    ),
    path(
        "categories/<str:slug>/",
        CategoryViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="category-detail",
    ),
    path(
        "products/",
        ProductViewSet.as_view({"get": "list", "post": "create"}),
        name="product-list",
    ),
    path(
        "products/<str:slug>/",
        ProductViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="product-detail",
    ),
]
