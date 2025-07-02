from django.shortcuts import render

from .models import Person
# Create your views here.
def home(request):
    return render(request , "index.html")
def person_list(request):
    person = Person.objects.all()
    return render (
        request, template_name= "person_list.html", context= {"persons" : person}
    )