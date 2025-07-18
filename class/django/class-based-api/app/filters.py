import django_filters

from .models import TodoModel


class TodoFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status", lookup_expr="exact")
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = TodoModel
        fields = ["status", "title"]
