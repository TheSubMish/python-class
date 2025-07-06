from django.urls import path
from .views import homepage,allBlog

urlpatterns = [
    path('',homepage),
    path('home/',homepage,name="home"),
    path('allblog/',allBlog,name="allblog"),
]
