from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import TodoModel
from .serializers import TodoSerializer
from .filters import TodoFilter


class TodoListView(APIView):

    def get_queryset(self, request):

        status_filter = request.query_params.get("status", None)
        if status_filter:
            return TodoModel.objects.filter(status=status_filter)

        title_filter = request.query_params.get("title", None)
        if title_filter:
            return TodoModel.objects.filter(title__icontains=title_filter)

        return TodoModel.objects.all()

    def get(self, request):
        todos = self.get_queryset(request)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return TodoModel.objects.get(pk=pk)
        except TodoModel.DoesNotExist:
            return None

    def get(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(
                {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(
                {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            updated_todo = serializer.save()
            return Response(
                TodoSerializer(updated_todo).data, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(
                {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            updated_todo = serializer.save()
            return Response(
                TodoSerializer(updated_todo).data, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(
                {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
            )

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TodoViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"
    filterset_class = TodoFilter

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     status_filter = self.request.query_params.get("status", None)
    #     if status_filter:
    #         queryset = queryset.filter(status=status_filter)

    #     title_filter = self.request.query_params.get("title", None)
    #     if title_filter:
    #         queryset = queryset.filter(title__icontains=title_filter)

    #     return queryset

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     if pk is None:
    #         return None
    #     try:
    #         return TodoModel.objects.get(pk=pk)
    #     except TodoModel.DoesNotExist:
    #         return None
