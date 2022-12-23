from rest_framework import serializers

from user.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'content',
            'author',
            'date_created',
            'likes',
            'get_absolute_url',
        )
