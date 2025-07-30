from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

from .models import note
from .forms import registerForm,loginForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if User.objects.filter(username=username).exists():
                return HttpResponse("username already used")
            
            if User.objects.filter(email=email).exists():
                return HttpResponse("email already used")
            
            if username and email and password:
                User.objects.create_user(
                    username=username, email=email, password=password
                )
                return redirect('login')

    else:
        form = registerForm()

    return render(
        request,
        "registration/registration.html",
        {
            "form" : form
        }
    )

def loginUser(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                login(request,user)
                return redirect('home')

    else:
        form = loginForm()

    return render(
        request,
        "registration/login.html",
        {
            "form" : form
        }
    )

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    data = note.objects.filter(user=request.user)

    return render(
        request,
        "home.html",
        {
            "data": data,
        }
    )

@login_required
def addNote(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        note.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('home')

    return render(
        request,
        "addnote.html",
    )

@login_required
def update(request,pk):
    data = get_object_or_404(note, pk=pk, user=request.user)
    if request.method == "POST":
        newtitle = request.POST.get('title',data.title)
        newcontent = request.POST.get('content',data.content)
        
        if newtitle and newcontent:
            data.title = newtitle
            data.content = newcontent
            data.save()
            return redirect('home')

    return render(
        request,
        "update.html",
        {
            "data": data,
        }
    )

@login_required
def delete(request, pk):
    data = get_object_or_404(note, pk=pk, user=request.user)
    data.delete()
    return redirect('home')