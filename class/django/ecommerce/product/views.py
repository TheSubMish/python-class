from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer
from .models import Product, Category
from .permissions import IsAdminUser


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE", "PATCH"]:
            self.permission_classes = [permissions.IsAuthenticated, IsAdminUser]
        return super().get_permissions()


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE", "PATCH"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailSerializer
        return super().get_serializer_class()
