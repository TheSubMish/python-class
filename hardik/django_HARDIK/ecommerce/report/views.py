
from rest_framework import generics,permissions,exceptions
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter

from django.db.models import Sum, Count, Min

from order.models import Order

# Create your views here.
class OrderReport(generics.GenericAPIView):
    # permission_classes=[permissions.IsAuthenticated]

    def pardse_date(self,date_str):
        try:
            from datetime import datetime
            return datetime.strptime(date_str,"%Y-%m-%d").date()
        
        except ValueError:
            raise exceptions.ValidationError("Invalid date")
        
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="start_date",
                type=str,
                location=OpenApiParameter.QUERY,
                description="date format in YYYY-MM-DD",
                required=True
            ),
            OpenApiParameter(
                name="end_date",
                type=str,
                location=OpenApiParameter.QUERY,
                description="date format in YYYY-MM-DD",
                required=True
            )
        ],
        responses={
            "application/json":{
                "example":{
                    "orders":{
                        "id":"1",
                        "total_amount":100.0,
                        "created_at":"2025-3-18",
                    }
                }
            }
        }
    )

    def get(self,request,*args,**kwargs):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        
        user = request.user
        if not start_date or not end_date:
            raise exceptions.ValidationError("Date not provided")
        
        parsed_start_date= self.pardse_date(start_date)
        parsed_end_date= self.pardse_date(end_date)

        orders= Order.objects.filter(
            created_at__gte = parsed_start_date, 
            created_at__lte = parsed_end_date
        )

        if user.is_authenticated and user.role == "customer":
            orders = orders.filter(user=user)
            order_data = [
                {
                "id":str(order.pk),
                "total_amount": float(order.gross_amount),
                "created_at": order.created_at.isoformat() 
            }
            for order in orders
        ]
            
        else:
            orders = orders.values(
                "user__id","user__username","created_at"
            ).annotate(
                total_amount=Sum("gross_amount"),
                total_order= Count("id")
            )

            order_data=[
                {
                    "id":str(order["user__id"]),
                    "customer": str(order["user_username"]),
                    "total_amount":float(order["total_amount"]),
                    "total_order":int(order["total_order"]),
                    "created_at":(
                        order["created_at"].isoformat()
                        if order["created_at"]
                        else None
                    )
                }
                for order in orders
            ]

        return Response({"orders":order_data})

