from rest_framework import serializers

from .models import Order, OrderItem, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class CustomerDetailsSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=255, required=False)
    phone = serializers.CharField(max_length=20, required=False)
    email = serializers.EmailField(required=False)


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    customer_details = CustomerDetailsSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        order_items_data = validated_data.pop("order_items")
        customer_details_data = validated_data.pop("customer_details", {})
        order = Order.objects.create(
            **validated_data, customer_details=customer_details_data
        )

        net_amount, discount = 0, 0

        for item_data in order_items_data:
            item = OrderItem.objects.create(order=order, **item_data)
            item.total_price = item.quantity * item.price
            item.save()

            net_amount += item.total_price
            discount += (
                item.total_price * item.product.discount if item.product.discount else 0
            )

        order.net_amount = net_amount  # type: ignore
        order.discount = discount  # type: ignore
        order.gross_amount = net_amount + order.tax_amount - discount  # type: ignore
        order.save()

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
