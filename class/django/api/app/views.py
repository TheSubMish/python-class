from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json

from .models import TodoModel


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
