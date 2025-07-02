from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField()


    # def __str__(self):
        # return f"Hello {self.name} {self.age} {self.email} {self.address}"


