from django.db import models

# Create your models here.
class car(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, Price: {self.price}"