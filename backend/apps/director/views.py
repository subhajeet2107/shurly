from django.conf import settings
from django.template.loader import render_to_string

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from apps.director.models import Director
from apps.director.serializers import DirectorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = []

    def perform_create(self, serializer):
        director = serializer.save()
