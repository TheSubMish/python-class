from rest_framework import serializers
from .models import Product,Category,SubCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
  
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['category','name']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)  
    class Meta:
        model = Category
        fields = ['id', 'name','subcategories']

class ProductDetailsSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    class Meta:
        model = Product
        fields = "__all__"