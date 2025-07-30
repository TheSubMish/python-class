from django.urls import path

# from .views import add_restaurant,update_restaurant,add_menu,update_menu
from .views import RestaurantOptions,MenuOptions


urlpatterns = [
    path('restaurant/',RestaurantOptions.as_view({"get":"list","post":"create"})),
    path('restaurant/<int:pk>/',RestaurantOptions.as_view({"get":"retrieve",'put':'update','patch':'partial_update','delete':'destroy'})),
    path('menu/',MenuOptions.as_view({'get':'list','post':'create'})),
    path('menu/<int:pk>/',MenuOptions.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),

    # path('addrestaurant/',add_restaurant,name="addrestaurant"),
    # path('updaterestaurant/<int:pk>/',update_restaurant,name="updaterestaurant"),
    # path('addmenu/',add_menu,name="addmenu"),
    # path('updatemenu/<int:pk>/',update_menu,name="updatemenu"),
]