from django.db import models

# Create your models here.

class baseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class contents(baseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/images',null=True,blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"Title: {self.title}"
    
class Author(baseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
    
class comments(baseModel):
    blog = models.ForeignKey(contents,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment: {self.comment}"