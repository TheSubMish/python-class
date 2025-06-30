from django.shortcuts import render

from .models import Person

from django.http import HttpResponse

from datetime import datetime

# Create your views here.


def create_person(name, age, email, address=None):
    # Example of creating a new Person instance
    person = Person.objects.create(name=name, age=age, email=email, address=address)

    print(f"New person created with name: {person.name}")

def home_page(request):
    
    if request.method == "POST":
        print("Received a POST request")
        
        print("Request data:", request.POST)
        
        name = request.POST.get("name", "Default Name")
        age = request.POST.get("age", "Default Age")
        email = request.POST.get("email", "Default Email")
        address = request.POST.get("address", "Default Address")
        
        print(f"Name: {name}, Age: {age}, Email: {email}, Address: {address}")
        
        create_person(name,age,email,address)
        
        return render(
            request,
            template_name="index.html",
            context={
                "message": "This is the index page of the second project.",
                "name": name,
                "age": age,
                "email": email,
                "address": address,
                "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    
    print("Request method:", request.method)  # Print the request method for debugging
    # request.method = "GET"

    result = 10 + 30  # Example operation
    print(f"Result of the operation: {result}")  # Print to console for debugging


    # return HttpResponse(
    #     f"Hello, world! This is the home page of my Django app.{result}"
    # )

    return render(
        request,
        template_name="index.html",
        context={
            "message": "This is the index page of the second project.",
            "result": result,
            "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
