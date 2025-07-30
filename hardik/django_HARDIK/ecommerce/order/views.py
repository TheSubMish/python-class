from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CartSerializer,OrderItemSerializer,OrderSerializer,CustomerSerializer
from .models import Cart,Order,OrderItem
# Create your views here.
class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "slug"

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "slug"

class OrderItemView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = "slug"

class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer