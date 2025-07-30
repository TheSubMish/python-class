import django_filters 

from .models import Note

class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = ['title','status']

    title = django_filters.CharFilter(field_name="title",lookup_expr="icontains")
    status = django_filters.CharFilter(field_name="status",lookup_expr="exact")