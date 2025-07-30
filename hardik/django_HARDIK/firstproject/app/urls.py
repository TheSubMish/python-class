from django.urls import path
from .views import homepage,carList,sellCar

urlpatterns = [
    path('',homepage,name="home"),
    path('home/',homepage,name="home"),
    path('list/',carList,name="carList"),
    path('sell/',sellCar,name="sell"),
]
