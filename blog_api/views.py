from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Note
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import serializers


class NoteListCreateAPIView(APIView):

    def get(self, request):
        obj = Note.objects.all()

        return Response([serializers.note_to_json(note) for note in obj])

    def post(self, request):
        data = request.data
        note = Note(**data)

        note.save(force_insert=True)

        return Response(serializers.note_created(note), status=status.HTTP_201_CREATED)

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




