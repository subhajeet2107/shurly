from rest_framework import serializers

from django.conf import settings
from apps.director.models import Director

from apps.users.serializers import UserSerializer


class DirectorSerializer(serializers.ModelSerializer):
    updated_on = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    users = UserSerializer(many=True)

    class Meta:
        model = Director
        fields = ['original_url', 'short_url', 'updated_on','users']
