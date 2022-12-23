from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "date_joined",
            "get_profile_picture",
            "bio",
            "liked_posts",
            "followers",
            "following",
            "slug"
        )
