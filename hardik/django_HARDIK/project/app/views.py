from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import NoteSerializer

from .models import Note,Status

# Create your views here.
    
@api_view(["GET","POST"])
def serializerAPI(request):
    if request.method == "GET":
        note = Note.objects.all()

        filter_title = request.query_params.get("title",None)

        if filter_title:
            note = note.filter(title__icontains= filter_title)

        filter_status = request.query_params.get("status",None)
        if filter_status:
            if filter_status not in Status.values:
                return Response(
                    status=status.HTTP_404_NOT_FOUND
                )
            
            note = note.filter(status=filter_status)

        serializer = NoteSerializer(note, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            new = serializer.save()
            return Response(NoteSerializer(new).data,status=status.HTTP_201_CREATED)
        
@api_view(["GET","PUT","PATCH","DELETE"])
def serializer2(request,pk):
    try:
        note = Note.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = NoteSerializer(note,data = request.data)
        if serializer.is_valid():
            updated = serializer.save()
            return Response(NoteSerializer(updated).data,status=status.HTTP_200_OK)
        
    if request.method == "PATCH":
        serializer = NoteSerializer(note,data = request.data, partial = True)
        if serializer.is_valid():
            patch = serializer.save()
            return Response(NoteSerializer(patch).data,status=status.HTTP_200_OK)

    if request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


