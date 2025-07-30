from django.urls import path

from .views import CartView,OrderItemView,OrderView,CustomerView

urlpatterns = [
    path("cartview/",CartView.as_view({"get": "list", "post": "create"})),
    path("cartview/<str:slug>/",CartView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("orderitem/",OrderItemView.as_view({"get": "list", "post": "create"})),
    path("orderitem/<str:slug>/",OrderItemView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("order/",OrderView.as_view({"get": "list", "post": "create"})),
    path("order/<str:slug>/",OrderView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))

]