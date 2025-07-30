from django.urls import path

from .views import OrderReport

urlpatterns=[
    path('orderreport/',OrderReport.as_view(),name='order_report'),
]