from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import AuthorForm, BlogForm, CommentForm, UserForm, LoginForm
from .models import Blog, Comment, Author

# Create your views here.


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")

            # Check if the user already exists
            if User.objects.filter(username=username).exists():
                return HttpResponse(
                    "Username already exists. Please choose a different one."
                )

            # Create the user
            if username and password and email:
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                return redirect("login_view")

        else:
            return HttpResponse(
                "Invalid form submission. Please check the data and try again."
            )

    form = UserForm()
    return render(request, "registration/user_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            # Log the user in
            login(request, user)
            return redirect("blog_list_create")
        else:
            return HttpResponse("Invalid username or password.")

    return render(request, "registration/login.html")


def logout_view(request):
    print(request.user)

    print(
        "Logging out user:",
        request.user.username if request.user.is_authenticated else "Anonymous",
    )
    print(request.user.first_name)
    print(request.user.last_name)
    print(request.user.email)
    # Log out the user
    logout(request)
    return redirect("login_view")


@login_required
def author_create_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list_create")
        else:
            # redirect("error_page")
            return HttpResponse(
                "Invalid form submission. Please check the data and try again."
            )
    else:
        form = AuthorForm()
    return render(request, "author_form.html", {"form": form})


def blog_create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blog_list_create")
    else:
        form = BlogForm()

        author = Author.objects.all()
    return render(request, "blog_form.html", {"form": form, "author": author})


def comment_create_view(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return redirect("error_page")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect("blog_detail_update_delete", pk=blog_id)
    else:
        form = CommentForm()
    return render(request, "comment_form.html", {"form": form, "blog": blog})


def error_page(request):
    return render(request, "error.html", {"message": "An error occurred."})


@login_required
def blog_get_post_view(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        # image = request.POST.get("image",None)

        # print(image)

        # if image is None:
        image = request.FILES.get("image")

        print("Request POST Data:", request.POST)
        print("Request FILES Data:", request.FILES)

        print(image)

        if title and content:
            blog = Blog.objects.create(title=title, content=content, image=image)
            return redirect("blog_list_create")
        else:
            return redirect("error_page")

    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
    }

    return render(request, "blog_list.html", context)


def blog_detail_update_delete_view(request, pk):

    print("Request Method:", request.method)

    try:

        blog = Blog.objects.get(pk=pk)

    except Blog.DoesNotExist:
        return redirect("error_page")

    if request.method == "POST":
        # title = request.query_params.get("title", blog.title)
        # content = request.query_params.get("content", blog.content)
        title = request.POST.get("title", blog.title)
        content = request.POST.get("content", blog.content)

        print(request.POST)
        print(request.FILES)

        image = request.POST.get("image", blog.image)

        if title and content:
            blog.title = title
            blog.content = content
            blog.image = image
            blog.save()
            return redirect("blog_list_create")

    elif request.method == "DELETE":
        blog.delete()
        return redirect("blog_list_create")

    comments = Comment.objects.filter(blog=blog)

    return render(request, "blog_details.html", {"blog": blog, "comments": comments})


def blog_delete_view(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return redirect("error_page")

    blog.delete()
    return redirect("blog_list_create")
