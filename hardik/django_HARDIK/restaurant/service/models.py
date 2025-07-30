from django.db import models

# Create your models here.
class Location(models.TextChoices):
    CHITWAN = 'chitwan', 'Chitwan'
    KATHMANDU = 'kathmandu', 'Kathmandu' 
    POKHARA = 'pokhara','Pokhara'

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(
        max_length=30,
        choices=Location.choices,
    )
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()

