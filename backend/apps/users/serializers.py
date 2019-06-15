from rest_framework import serializers

from django.conf import settings

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    updated_on = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        return obj.avatar.url if obj.avatar else settings.STATIC_URL + 'images/default_avatar.png'

    class Meta:
        model = User
        fields = ['id','email', 'avatar', 'name', 'updated_on']


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'name']
