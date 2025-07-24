from django.db import models
from common.models import BaseModel

# Create your models here.


class Payment(BaseModel):
    order = models.ForeignKey(
        "order.Order", related_name="payments", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
    )
    transaction_id = models.CharField(
        max_length=100, unique=True, null=True, blank=True
    )

    def __str__(self):
        return f"Payment {self.pk} for Order {self.order.pk}"


class Invoice(BaseModel):
    order = models.ForeignKey(
        "order.Order", related_name="invoices", on_delete=models.CASCADE
    )
    invoice_number = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ("unpaid", "Unpaid"),
            ("paid", "Paid"),
            ("overdue", "Overdue"),
        ],
    )

    def __str__(self):
        return f"Invoice {self.invoice_number} for Order {self.order.pk}"


class InvoiceLineItem(BaseModel):
    invoice = models.ForeignKey(
        Invoice, related_name="line_items", on_delete=models.CASCADE
    )
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Line Item {self.pk} for Invoice {self.invoice.invoice_number}"
