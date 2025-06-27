from django.shortcuts import render

from .models import Person

from django.http import HttpResponse

# Create your views here.


def create_person():
    # Example of creating a new Person instance
    person = Person.objects.create(name="John Doe", age=30, email="kdksdj")


def home_page(request):

    result = 10 + 20  # Example operation
    print(f"Result of the operation: {result}")  # Print to console for debugging

    create_person()

    return HttpResponse(
        f"Hello, world! This is the home page of my Django app.{result}"
    )
