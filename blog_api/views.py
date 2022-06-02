from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

from blog.models import Note
from . import serializers, filters


class NoteListCreateAPIView(APIView):

    def get(self, request):
        obj = Note.objects.all().filter(public=True)
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


class NoteDetailAPIView(APIView):

    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = serializers.NoteDetailSerializer(
            instance=note,
        )

        return Response(serializer.data)

    def patch(self, request, pk):

        note = Note.objects.filter(pk=pk, author=request.user).first()
        if not note:
            raise NotFound(f'Статья с id={id} для пользователя {request.user.username} не найдена')

        new_note = serializers.NoteDetailSerializer(note, data=request.data, partial=True)

        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data, status=status.HTTP_200_OK)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = Note.objects.filter(pk=pk, author=request.user)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def filter_queryset(self, queryset):
        queryset = filters.important_filter(
            queryset,
            important=self.request.query_params.get("important")
        )
        queryset = filters.public_filter(
            queryset,
            public=self.request.query_params.get("public")
        )
        return queryset


