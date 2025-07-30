from django.shortcuts import render
from rest_framework import permissions

from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer,CategorySerializer,ProductDetailsSerializer,SubCategorySerializer


from .models import Product,Category,SubCategory
from .permissions import IsAdminUser

from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes =[]

    def get_permissions(self):
        if self.request.method in ["POST","PUT","PATCH","DELETE"]:
            self.permission_classes = [permissions.IsAuthenticated,IsAdminUser]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailsSerializer
        return super().get_serializer_class()
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method in ["POST","PUT","PATCH","DELETE"]:
            self.permission_classes = [permissions.IsAuthenticated,IsAdminUser]
        return super().get_permissions()

class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field='pk'
    permission_classes = []

    def get_permissions(self):
        if self.request.method in ["POST","PUT","PATCH","DELETE"]:
            self.permission_classes = [permissions.IsAuthenticated,IsAdminUser]
        return super().get_permissions()

