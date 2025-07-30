from django.shortcuts import render,redirect,HttpResponse

from .models import contents,Author
from .forms import authorForm,contentForm,userForm,loginForm

from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            if User.objects.filter(username=username).exists():
                return HttpResponse("USER ALREADY EXISTS.")
            
            if username and email and password:
                User.objects.create_user(
                    username=username,email=email,password=password
                )
                return redirect("login")
        
        else:
            return HttpResponse(
                "INVALID INPUTS"
            )
    else:
        form = userForm()

    return render(
        request,
        "register/register.html",
        {
            "form" : form
        }
    )

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pasword = request.POST.get("password")
        
        user = User.objects.filter(username=username).first()

        if user and user.check_password(pasword):
            login(request,user)
            return redirect('home')
        
    else: 
        form = loginForm()
    
    return render(
        request,
        "register/login.html",
        {
            "form" : form
        }
    )

def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required
def homepage(request):
    if request.method == "POST":
        form = contentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  
        else:
            return redirect("error")
    else:
        form = contentForm()
    return render(
        request, 
        "index.html", 
        {"form": form})

def author(request):
    if request.method == "POST":
        form = authorForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Author.objects.filter(email=email).exists():
                form.add_error('email','This email is already in use.')
            else:
                form.save()
                return redirect("home")
        else:
            return redirect("error")
    else:
        form = authorForm()
    return render(
        request,
        "authorform.html",
        {
            "form" : form,
        }
    )

def allBlog(request):
    cont = contents.objects.all()
    return render(
        request,
        "allblogs.html",
        {
            "contents": cont
        }
    )

def detailsPage(request,pk):
    try:
        view = contents.objects.get(pk=pk)
    except Exception:
        return render(
            request,
            "error.html"
        )
    
    return render(
        request,
        "details.html",
        {
            "blog" : view
        }
    )

def delete(pk):
    view = contents.objects.get(pk=pk)
    view.delete()
    return redirect("allblog")

def edit(request, pk):
    try:
        view = contents.objects.get(pk=pk)
    except:
        return render(request, "error.html")

    author = Author.objects.all()

    if request.method == "POST":
        newtitle = request.POST.get("title", view.title)
        newcontent = request.POST.get("content", view.content)
        newimage = request.FILES.get("image")
        newauthor = request.POST.get("author",view.author.id) 

        if newtitle and newcontent:
            view.title = newtitle
            view.content = newcontent

            if newimage:
                view.image = newimage 

            view.author = Author.objects.get(id=newauthor)
            view.save()
            return redirect('allblog')

    return render(
        request,
        "edit.html",
        {
            "blog": view,
            "authors": author
        }
    )


def errorPage(request):
    return render(
        request,
        "error.html"
    )