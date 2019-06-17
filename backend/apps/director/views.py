from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.db.models import F

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from apps.director.models import Director
from apps.director.serializers import DirectorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        original_url = request.data.get('original_url')

        if Director.objects.filter(original_url=original_url).exists():
            director = Director.objects.get(original_url=original_url)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            director = self.perform_create(serializer)

        director.refresh_from_db()
        serializer = DirectorSerializer(instance=director)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_authenticated:
            director = serializer.save(added_by=self.request.user)
        else:
            director = serializer.save()
        return director

    def perform_destroy(self, instance):
        instance.delete()


def redirector(request, short_url_hash):
    director = get_object_or_404(Director, short_url_hash=short_url_hash)
    director.hits = director.hits + 1
    director.save()
    return HttpResponsePermanentRedirect(director.original_url)

