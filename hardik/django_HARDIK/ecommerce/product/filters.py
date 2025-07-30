import django_filters

from .models import Product,Category,SubCategory

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name','category','subcategory']

    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')   
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategory = django_filters.ModelChoiceFilter(queryset=SubCategory.objects.all())

