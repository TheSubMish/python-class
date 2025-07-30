from django.shortcuts import render

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import NoteSerializer
from .models import Note

from .filters import NoteFilter

# Create your views here.
class NoteView(APIView):
    def get_queryset(self, request):
        note = Note.objects.all()
        filter_status = request.query_params.get("status",None)
        if filter_status:
            note = note.filter(status=filter_status)

        return note
    
    def get(self, request):
        notes = self.get_queryset(request)
        serializer = NoteSerializer(notes,many = True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self,request):
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            note = serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )

class NoteDetails(APIView):
    def get_object(self,request,pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return None
        
    def get(self,request,pk):
        note = self.get_object(request,pk)
        serializer = NoteSerializer(note)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
        
    def put(self,request,pk):
        note = self.get_object(request,pk)
        serializer = NoteSerializer(note, data = request.data)
        if serializer.is_valid():
            new = serializer.save()
            return Response(
                NoteSerializer(new).data,
                status=status.HTTP_200_OK
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self,request,pk):
        note = self.get_object(request,pk)
        serializer = NoteSerializer(note, data = request.data,partial = True)
        if serializer.is_valid():
            new = serializer.save()
            return Response(
                NoteSerializer(new).data,
                status=status.HTTP_200_OK
            ) 
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )       

    def delete(self,request,pk):
        note = self.get_object(request,pk)
        note.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'
    filterset_class = NoteFilter
