from django.urls import path

from .views import ProductViewSet,CategoryViewSet,SubCategoryViewSet

urlpatterns = [
    path("categories/",CategoryViewSet.as_view({"get": "list", "post": "create"})),
    path("categories/<str:slug>/",CategoryViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("subcategories/",SubCategoryViewSet.as_view({"get": "list", "post": "create"})),
    path("subcategories/<str:slug>/",SubCategoryViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("products/",ProductViewSet.as_view({"get": "list", "post": "create"})),
    path("products/<str:slug>/",ProductViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))
]