from django.contrib import admin
from django.urls import path
from .views import register,loginUser,home,logoutUser,addNote,update,delete

urlpatterns = [
    path('register/',register, name="register"),
    path('login/',loginUser,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('',home,name="home"),
    path('home/',home,name="home"),
    path('addnote/',addNote,name="addnote"),
    path('update/<int:pk>/',update,name="update"),
    path('delete/<int:pk>/', delete, name='delete'),
]