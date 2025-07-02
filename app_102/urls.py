
from django.urls import path
from .views import home, person_list
urlpatterns = [
        path("home", home),
        path('person/', person_list)


]    