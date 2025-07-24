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
    cart_items = serializers.ListSerializer(
        child=serializers.UUIDField(), required=False, allow_empty=True
    )

    # order_items = OrderItemSerializer(many=True)
    customer_details = CustomerDetailsSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        order_items_data = validated_data.pop("cart_items")
        customer_details_data = validated_data.pop("customer_details", {})
        order = Order.objects.create(
            **validated_data, customer_details=customer_details_data
        )

        net_amount, discount = 0, 0

        items_data = CartItem.objects.filter(id__in=order_items_data)

        for item_data in items_data:
            item = OrderItem.objects.create(
                order=order,
                product=item_data.product,
                quantity=item_data.quantity,
                price=item_data.product.price,
                total_price=item_data.quantity * item_data.product.price,
            )

            net_amount += item.total_price
            discount += (
                item.total_price * item.product.discount if item.product.discount else 0
            )

        order.net_amount = net_amount  # type: ignore
        order.discount = discount  # type: ignore
        order.gross_amount = net_amount + order.tax_amount - discount  # type: ignore
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
