from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json

from .models import TodoModel
from .serializers import TodoSerializer


@api_view(["GET"])
def simple_api(request):

    data = {
        "str": "Hello, World!",
        "int": 42,
        "float": 3.14,
        "bool": True,
        "list": [1, 2, 3],
        "dict": {"key": "value"},
        "null": None,
    }

    print(type(data))

    json_data = json.dumps(data)

    print(json_data)
    print(type(json_data))

    return Response(json_data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def todo_list(request):
    if request.method == "GET":

        todo = TodoModel.objects.all()

        print(type(todo))

        todo_list = list(todo.values())

        return Response(todo_list, status=status.HTTP_200_OK)

    if request.method == "POST":
        title = request.data.get("title")
        if not title:
            return Response(
                {"error": "Title is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        todo = TodoModel.objects.create(title=title)

        return Response(
            {"id": todo.pk, "title": todo.title}, status=status.HTTP_201_CREATED
        )

    return Response(
        {"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


@api_view(["GET", "POST", "PUT", "DELETE"])
def serializer_api_example(request):
    if request.method == "GET":
        todos = TodoModel.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            todo = serializer.save()
            return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail(request, pk):
    try:
        todo = TodoModel.objects.get(pk=pk)
    except TodoModel.DoesNotExist:
        return Response({"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":

        print("Updating todo with ID:", pk, request.method)

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            updated_todo = serializer.save()
            return Response(
                TodoSerializer(updated_todo).data, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializer = TodoSerializer(todo, data=request.data, partial=True)

        if serializer.is_valid():
            updated_todo = serializer.save()
            return Response(
                TodoSerializer(updated_todo).data, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(
        {"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )
