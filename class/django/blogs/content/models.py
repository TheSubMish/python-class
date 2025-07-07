from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Blog(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/images/', null=True, blank=True)

    def __str__(self):
        return self.title


# blogs = Blog.objects.first().comments.all()
# commentsset

class Comment(BaseModel):
    blog = models.ForeignKey(Blog,  related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment on {self.blog.title} by {self.created_at}"
