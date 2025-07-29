from django.urls import path


from .views import OrderReportView


urlpatterns = [
    path("order/", OrderReportView.as_view(), name="order-report"),
]
