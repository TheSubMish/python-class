from django.urls import path

from .views import serializerAPI,serializer2

urlpatterns = [
    path('serializerapi/',serializerAPI,name='serializerapi'),
    path('serializer2/<int:pk>/',serializer2,name='serializer2'),
]