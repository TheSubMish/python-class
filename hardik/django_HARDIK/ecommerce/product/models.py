from django.db import models
from decimal import Decimal

from django.utils.text import slugify

from common.models import Creation

# Create your models here.
class Category(Creation):
    name =models.CharField(max_length=10)
    slug = models.SlugField(max_length=50,unique=True, null=True,blank=True)

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
class SubCategory(Creation):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="subcategories")
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=50,unique=True, null=True,blank=True)

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)


class Product(Creation):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.00), null=True, blank=True,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name="products")
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True, related_name="products")
    slug = models.SlugField(max_length=50,unique=True, null=True,blank=True)

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

