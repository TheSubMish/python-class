from django.urls import path

from .views import NoteView,NoteDetails,NoteViewSet

urlpatterns = [
    path('view/',NoteView.as_view(),name="view"),
    path('view/<int:pk>/',NoteDetails.as_view(),name="details"),
    path('note/',NoteViewSet.as_view({"get":"list","post":"create"})),
    path('note/<int:pk>/',NoteViewSet.as_view({"get":"retrieve","put":"update","patch":"partial_update","delete":"destroy"})),
]