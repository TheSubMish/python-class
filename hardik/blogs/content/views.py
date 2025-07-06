from django.shortcuts import render
from .models import contents

def addContent(title,content,author):
    contents.objects.create(title=title,content=content,author=author)

# Create your views here.
def homepage(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")
        addContent(title,content,author)

        return render(
        request,
        "index.html",
        {
            "message": "Blog Added"
        }
        )

    return render(
        request,
        "index.html",
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