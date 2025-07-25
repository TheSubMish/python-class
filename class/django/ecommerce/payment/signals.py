from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete


from .models import Payment, Invoice, InvoiceLineItem
from order.models import OrderItem


@receiver(post_save, sender=Payment)
def create_invoice(sender, instance, created, **kwargs):

    if instance.status == "completed":
        invoice = Invoice.objects.create(
            order=instance.order,
            total_amount=instance.amount,
            status="paid",
            issue_date=instance.created_at.date(),
            due_date=instance.created_at.date(),  # Assuming due date is same as issue date
        )
        order_items = OrderItem.objects.filter(order=instance.order)
        for item in order_items:
            InvoiceLineItem.objects.create(
                invoice=invoice,
                product=item.product,
                quantity=item.quantity,
                price=item.price,
            )

        instance.order.status = "Completed"
        instance.order.save()
