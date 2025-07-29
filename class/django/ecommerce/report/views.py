from rest_framework import generics, exceptions, permissions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from django.db.models import Sum, Count, Min

from order.models import Order


class OrderReportView(generics.GenericAPIView):

    # permission_classes = [permissions.IsAuthenticated]

    def parse_date(self, date_str):
        try:
            from datetime import datetime

            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise exceptions.ValidationError("Invalid date format. Use YYYY-MM-DD.")

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="start_date",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Start date for the report in YYYY-MM-DD format.",
                required=True,
            ),
            OpenApiParameter(
                name="end_date",
                type=str,
                location=OpenApiParameter.QUERY,
                description="End date for the report in YYYY-MM-DD format.",
                required=True,
            ),
        ],
        responses={
            "application/json": {
                "example": {
                    "orders": [
                        {
                            "id": "1",
                            "total_amount": 100.0,
                            "created_at": "2023-01-01T00:00:00Z",
                        }
                    ]
                }
            }
        },
    )
    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        user = request.user

        if not start_date or not end_date:
            raise exceptions.ValidationError(
                "Both start_date and end_date are required."
            )

        parsed_start_date = self.parse_date(start_date)
        parsed_end_date = self.parse_date(end_date)

        orders = Order.objects.filter(
            created_at__date__gte=parsed_start_date,
            created_at__date__lte=parsed_end_date,
        )

        if user.is_authenticated and user.role == "customer":
            orders = orders.filter(user=user)

            # list comprehension to create a list of dictionaries
            orders_data = [
                {
                    "id": str(order.pk),
                    "total_amount": float(order.gross_amount),
                    "created_at": order.created_at.isoformat(),
                }
                for order in orders
            ]

            # Alternatively, if you want to use a loop instead of list comprehension
            orders_data = []
            for order in orders:
                orders_data.append(
                    {
                        "id": str(order.pk),
                        "total_amount": float(order.gross_amount),
                        "created_at": order.created_at.isoformat(),
                    }
                )
        else:
            # Group by user and date, aggregate total_amount and total_orders
            orders = orders.values(
                "user__id", "user__username", "created_at__date"
            ).annotate(
                total_amount=Sum("gross_amount"),
                total_orders=Count("id"),
            )

            orders_data = [
                {
                    "id": str(order["user__id"]),
                    "customer": order["user__username"],
                    "total_amount": float(order["total_amount"]),
                    "total_orders": order["total_orders"],
                    "created_at": (
                        order["created_at__date"].isoformat()
                        if order["created_at__date"]
                        else None
                    ),
                }
                for order in orders
            ]

        return Response({"orders": orders_data})


# ids
Order.objects.filter(id__in=[1, 2, 3])
