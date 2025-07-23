from django.db import models
from django.utils.text import slugify
from decimal import Decimal


from common.models import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal(0.00), null=True, blank=True
    )

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
