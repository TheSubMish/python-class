from django.shortcuts import render, redirect
from .forms import AuthorForm, BlogForm, CommentForm

from .models import Blog, Comment, Author

# Create your views here.


def author_create_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list_create")
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
