from rest_framework import serializers

from django.conf import settings
from apps.director.models import Director

from apps.users.serializers import UserSerializer


class DirectorSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(read_only=True)
    short_url_hash = serializers.CharField(read_only=True)
    hits = serializers.CharField(read_only=True)
    updated_on = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    added_by = UserSerializer(read_only=True)

    class Meta:
        model = Director
        fields = ['original_url', 'short_url', 'short_url_hash', 'hits', 'updated_on','added_by']
