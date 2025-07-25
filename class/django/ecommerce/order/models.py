from django.db import models
from common.models import BaseModel
from decimal import Decimal
from product.models import Product
from auth.models import User


# Create your models here.
class CartItem(BaseModel):
    product = models.ForeignKey(
        Product, related_name="cart_items", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"


class OrderStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    COMPLETED = "Completed", "Completed"
    CANCELLED = "Cancelled", "Cancelled"
    
    
class PaymentStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    COMPLETED = "Completed", "Completed"
    FAILED = "Failed", "Failed"


class Order(BaseModel):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal(0.00)
    )
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal(0.00), null=True, blank=True
    )
    status = models.CharField(
        max_length=50, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    customer_details = models.JSONField(
        default=dict, help_text="Store customer details like address, phone, etc."
    )
    payment_status = models.CharField(
        max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )

    def __str__(self):
        return f"Order {self.pk} by {self.user.username} - Total: {self.gross_amount}"


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.order.user.username} - Total: {self.total_price}"
