from rest_framework import serializers

from .models import Restaurant,Menu

class Restaurant_serializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length = 50)
    # location = serializers.CharField(max_length = 50)

    # def create(self, validated_data):
    #     return Restaurant.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name",instance.name)
    #     instance.location = validated_data.get("location",instance.location)
    #     instance.save()
    #     return instance

class Menu_serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    # restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    # item_name = serializers.CharField(max_length=50)
    # price = serializers.IntegerField()

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['restaurant'] = instance.restaurant.name
    #     return rep
    
    # def create(self, validated_data):
    #     return Menu.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.item_name = validated_data.get("item_name",instance.item_name)
    #     instance.price = validated_data.get("price",instance.price)
    #     instance.save()
    #     return instance