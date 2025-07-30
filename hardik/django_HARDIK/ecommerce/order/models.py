from django.db import models
from decimal import Decimal

from product.models import Product
from common.models import Creation
from auth.models import User
# Create your models here.

class Cart(Creation):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="cart_item")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart_item")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    # def __str__(self):
    #     return self.user

class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    IN_PROGRESS = 'in_progress',"In_progress"
    COMPLETED = 'completed', 'Completed'
    CANCEL = 'cancel','Cancel'

class PaymentStatus(models.TextChoices):
    PENDING ='pending','Pending'
    COMPLETED = 'completed','Completed'
    FAILED = 'failed','Failed'

class Order(Creation):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    net_amount = models.DecimalField(max_digits=10,decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal(0.0))
    gross_amount = models.DecimalField(max_digits=10,decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal(0.0))
    status = models.CharField(max_length=15,choices=OrderStatus.choices,default=OrderStatus.PENDING)
    customer_details= models.JSONField(default=dict,help_text="Customer details")
    payment_status=models.CharField(max_length=10,choices=PaymentStatus.choices,default=PaymentStatus.PENDING)

class OrderItem(Creation):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    amount =models.DecimalField(max_digits=10,decimal_places=2)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)


