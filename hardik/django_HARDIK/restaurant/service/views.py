from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet

from .models import Restaurant,Menu

from .serializers import Restaurant_serializer,Menu_serializer

from .filters import MenuFilter

# Create your views here.

class RestaurantOptions(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = Restaurant_serializer
    lookup_field = "pk"

class MenuOptions(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = Menu_serializer
    lookup_field = "pk"
    filterset_class = MenuFilter

# @api_view(["GET","POST"])
# def add_restaurant(request):
#     if request.method == "GET":
#         data = Restaurant.objects.all()
#         filter_location = request.query_params.get("location", None)
#         if filter_location:
#             data = data.filter(location=filter_location)

#         serializer = Restaurant_serializer(data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         serializer = Restaurant_serializer(data = request.data)
#         if serializer.is_valid():
#             newdata = serializer.save()
#             return Response(
#                 Restaurant_serializer(newdata).data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","PATCH","DELETE"])
# def update_restaurant(request,pk):
#     try:
#         current_data = Restaurant.objects.get(pk=pk)
#     except Restaurant.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     if request.method == "GET":
#         serializer = Restaurant_serializer(current_data)
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )

#     if request.method == "PUT":
#         serializer = Restaurant_serializer(current_data,data=request.data)
#         if serializer.is_valid():
#             newdata = serializer.save()
#             return Response(
#                 Restaurant_serializer(newdata).data,
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "PATCH":
#         serializer = Restaurant_serializer(current_data,data=request.data,partial = True)
#         if serializer.is_valid():
#             newdata = serializer.save()
#             return Response(
#                 Restaurant_serializer(newdata).data,
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         current_data.delete()
#         return Response(
#                 status=status.HTTP_204_NO_CONTENT
#             )


# @api_view(["GET","POST"])
# def add_menu(request):
#     if request.method == "GET":
#         data = Menu.objects.all()
#         filter_item = request.query_params.get("item_name", None)
#         if filter_item:
#             data = data.filter(item_name__icontains=filter_item)

#         serializer = Menu_serializer(data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         serializer = Menu_serializer(data = request.data)
#         if serializer.is_valid():
#             newdata = serializer.save()
#             return Response(
#                 Menu_serializer(newdata).data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PATCH","DELETE"])
# def update_menu(request,pk):
#     try:
#         current_data = Menu.objects.get(pk=pk)
#     except Menu.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     if request.method == "GET":
#         serializer = Menu_serializer(current_data)
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )

#     if request.method == "PATCH":
#         serializer = Menu_serializer(current_data,data=request.data,partial = True)
#         if serializer.is_valid():
#             newdata = serializer.save()
#             return Response(
#                 Menu_serializer(newdata).data,
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         current_data.delete()
#         return Response(
#                 status=status.HTTP_204_NO_CONTENT
#             )

