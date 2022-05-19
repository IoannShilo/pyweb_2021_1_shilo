from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from blog.models import Note
from django.shortcuts import get_object_or_404
from . import serializers


class NoteListCreateAPIView(APIView):

    def get(self, request):
        obj = Note.objects.all()
        serializer = serializers.NoteSerializer(instance=obj, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.NoteSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(
            serializer.data
        )


class PublicNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)


class NoteDetailAPIView(APIView):

    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)

        return Response(serializers.note_to_json(note))

    def put(self, request, pk):
      data = request.data
      note = Note.objects.get(pk=pk)
      note.title = data['title']
      note.message = data['message']
      note.save()
      return Response(serializers.note_created(note), status=status.HTTP_200_OK)




