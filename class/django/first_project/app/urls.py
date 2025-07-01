from django.urls import path

from .views import home_page, person_list

urlpatterns = [
    path("", home_page, name="home"), # /app/
    path("persons/", person_list, name="person_list"),   # /app/persons/
]