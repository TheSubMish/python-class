import django_filters

from .models import Menu

class MenuFilter(django_filters.FilterSet):
    class Meta:
        model = Menu
        fields = ['item_name',]

    item_name = django_filters.CharFilter(field_name="item_name",lookup_expr="icontains",label='Search by Item Name')