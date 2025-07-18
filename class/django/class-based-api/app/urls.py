from django.urls import path
from .views import (
    TodoListView,
    TodoDetailUpdateDeleteView,
    TodoViewSet,
    TodoListCreateView,
)


urlpatterns = [
    path("todos/", TodoListView.as_view(), name="todo-list"),
    path("todos/<int:pk>/", TodoDetailUpdateDeleteView.as_view(), name="todo-detail"),
    # path(
    #     "todos/viewset/",
    #     TodoViewSet.as_view({"get": "list", "post": "create"}),
    #     name="todo-viewset",
    # ),
    path(
        "todos/viewset/",
        TodoListCreateView.as_view(),
        name="todo-list-create-viewset",
    ),
    path(
        "todos/viewset/<int:pk>/",
        TodoViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="todo-detail-viewset",
    ),
]
