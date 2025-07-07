from django.shortcuts import render, redirect

from .models import Blog, Comment

# Create your views here.


def error_page(request):
    return render(request, "error.html", {"message": "An error occurred."})


def blog_get_post_view(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            blog = Blog.objects.create(title=title, content=content)
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

        if title and content:
            blog.title = title
            blog.content = content
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
