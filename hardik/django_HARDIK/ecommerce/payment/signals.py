from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Payment,Invoice,InvoiceItem
from order.models import OrderItem

@receiver(post_save,sender = Payment)
def create_inivoice(sender,instance,created,**kwargs):
    if instance.status == 'completed':
        invoice = Invoice.objects.create(
            order=instance.order,
            total_amount = instance.total_amount,
            status = "paid",
            issued_date = instance.created_at
        )

        order_items = OrderItem.objects.filter(order=instance.order)
        for item in order_items:
            invoice_items = InvoiceItem.objects.create(
                product = item.product.name,
                quantity = item.quantity,
                amount= item.amount,
                total_amount= item.total_amount
            )
        instance.order.status == 'completed'
        instance.order.save()
