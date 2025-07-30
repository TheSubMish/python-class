from django.shortcuts import render
from .models import car

# Create your views here.

def addCar(name,year,price):
    return car.objects.create(name=name,year=year,price=price)

def homepage(request):
    cars = car.objects.all()
    return render(
            request,
            "index.html",
            {
                "cars" :cars,
            }
        )

def carList(request):
    cars = car.objects.all()
    return render(
            request,
            "carList.html",
            {
                "cars" :cars,
            }
        )

def sellCar(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        year = request.POST.get("year")
        price = request.POST.get("price")

        addCar(name,year,price)
        return render(request,"sell.html",
        {
            "name" : name,
            "year" : year,
            "price" : price,
        })
  
    return render(
            request,
            "sell.html"
        )