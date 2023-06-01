from django.contrib.auth import get_user_model

from rest_framework import serializers
# from post.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    liked_posts = serializers.SerializerMethodField()

    def get_followers(self, obj):
        return obj.followers.count()

    def get_following(self, obj):
        return obj.following.count()

    def get_liked_posts(self, obj):
        return obj.liked_posts.count()

    class Meta:
        model = get_user_model()

        fields = (
            "email",
            "username",
            "date_joined",
            "profile_picture",
            "get_profile_picture",
            "bio",
            "first_name",
            "last_name",
            "liked_posts",
            "followers",
            "following",
            "slug",
        )
