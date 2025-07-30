from django.db import models
from common.models import Creation
from order.models import Order
# Create your models here.

class Payment(Creation):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="payments",blank=True,null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices = [
            ('pending','Pending'),
            ('completed','Completed'),
            ('failed','Failed')
        ])
    transaction_id = models.CharField(max_length=200,unique=True,blank=True,null=True)

    def __str__(self):
        return f"{self.total_amount} paid through {self.payment_method}"

class Invoice(Creation):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="invoices",null=True,blank=True)
    invoice_no=models.CharField(max_length=100,unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date =models.DateField(blank=True,null=True)
    issued_date=models.DateField(blank=True,null=True)
    status = models.CharField(
        max_length=20,
        choices = [
            ('unpaid','Unpaid'),
            ('paid','Paid'),
            ('overdue','Overdue')
        ])
    def __str__(self):
        return f"Invoice No: {self.invoice_no}, Issued date: {self.issued_date}"
    
    def save(self,*args,**kwargs):
        last_invoice = Invoice.objects.filter(order=self.order).order_by('-id').first()
        if last_invoice:
            self.invoice_no = f"INV-{int(last_invoice.invoice_no.split('-')[1])+1}" if last_invoice.invoice_no else "INV-1"
        else:
            self.invoice_no = "INV-1"

        print("working fine")
        super().save(*args,**kwargs)
        print("working fine")
    
class InvoiceItem(Creation):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="invoiceitem")
    product = models.CharField(max_length=50)
    unit_amount=models.DecimalField(max_digits=10,decimal_places=2)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)

    # def __str__(self):
    #     return f"Invoice No: {self.invoice_no}, Issued date: {self.issued_date}"
    

    