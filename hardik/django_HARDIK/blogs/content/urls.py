from django.urls import path
from .views import homepage,allBlog,detailsPage,delete,edit,errorPage,author,registerUser,loginPage,logoutuser

urlpatterns = [
    path('',homepage),
    path('home/',homepage,name="home"),
    path('allblog/',allBlog,name="allblog"),
    path('<int:pk>/',detailsPage,name="detailsPage"),
    path('delete/<int:pk>/',delete,name="delete"),
    path('edit/<int:pk>/',edit,name="edit"),
    path('error/',errorPage,name="error"),
    path('authorform/',author,name="authorform"),
    path('register/',registerUser,name="register"),
    path('login/',loginPage,name="login"),
    path('logout/',logoutuser,name="logout"),
]
