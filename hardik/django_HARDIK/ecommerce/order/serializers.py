from rest_framework import serializers

from .models import Cart,Order,OrderItem
from product.models import Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class CustomerSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50,required=False)
    address=serializers.CharField(max_length=200,required=False)
    phone =serializers.CharField(max_length=15,required=False)    

class OrderSerializer(serializers.ModelSerializer):
    cart_items = serializers.ListSerializer(
        child=serializers.UUIDField(), required=False, allow_empty=True
    )
    customer_details=CustomerSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        order_item_data = validated_data.pop("cart_item")
        customer_details_data = validated_data.pop("customer_details",{})
        order = Order.objects.create(**validated_data,customer_details=customer_details_data)
        net_amount,discount =0,0
        items_data = Cart.objects.filter(id__in=order_item_data)

        for item in items_data:
            item = OrderItem.objects.create(
                order=order,
                product = item.product,
                quantity= item.quantity,
                amount=item.product.price,
                total_amount=item.quantity*item.product.price

                )
            

            net_amount+=item.total_amount
            discount+=(item.total_amount*item.product.discount if item.product.discount else 0)

        order.net_amount = net_amount
        order.discount_amount = discount
        order.gross_amount = order.net_amount+order.tax_amount-discount
        order.save()

        items_data.delete()
        return order
    
    def update(self, instance, validated_data):
        order_items_data = validated_data.pop("order_items", None)
        customer_details_data = validated_data.pop("customer_details", {})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if customer_details_data:
            instance.customer_details.update(customer_details_data)

        if order_items_data is not None:
            instance.order_items.all().delete()
            for item_data in order_items_data:
                OrderItem.objects.create(order=instance, **item_data)

        instance.save()
        return instance
    