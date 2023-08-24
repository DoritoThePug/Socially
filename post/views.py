from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from socially.authentication import CookieTokenAuthentication
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


# Create your views here.


class CreatePost(APIView):
    authentication_classes = (CookieTokenAuthentication, )

    def post(self, request, format=None):
        auth_token = request.COOKIES.get('token').split(' ')[1]

        author = Token.objects.get(key=auth_token).user

        post = Post(content=request.data['content'], author=author)

        post.save()

        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LatestPosts(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[0:10]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUserPosts(APIView):
    def get(self, request, user_slug, format=None):
        users = get_user_model()

        user = users.objects.get(slug=user_slug)

        if user is None:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)

        posts = Post.objects.filter(author=user)

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetail(APIView):
    def get(self, request, user_slug, post_id, format=None):
        users = get_user_model()

        user = users.objects.get(slug=user_slug)

        if user is None:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)

        post = Post.objects.get(author=user, id=post_id)

        if post is not None:
            serializer = PostSerializer(post)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Post not found", status=status.HTTP_404_NOT_FOUND)


class LikePost(APIView):
    authentication_classes = (CookieTokenAuthentication,)

    def patch(self, request, post_id, format=None):
        auth_token = request.COOKIES.get('token').split(' ')[1]

        user = Token.objects.get(key=auth_token).user

        post = Post.objects.get(id=post_id)

        if post is None:
            return Response("Post does not exist", status=status.HTTP_404_NOT_FOUND)

        if user in post.likes.all():
            post.likes.remove(user)
            user.liked_posts.remove(post)
        else:
            post.likes.add(user)
            user.liked_posts.add(post)

        post.save()
        user.save()

        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, post_id, format=None):
        auth_token = request.COOKIES.get('token').split(' ')[1]

        post = Post.objects.get(id=post_id)

        if post is None:
            return Response("Post does not exist", status=status.HTTP_404_NOT_FOUND)

        user = Token.objects.get(key=auth_token).user
        serializer = PostSerializer(post)

        if user in post.likes.all():
            return Response({"isLiked": True, "post": serializer.data}, status=status.HTTP_200_OK)

        return Response({"isLiked": False, "post": serializer.data}, status=status.HTTP_200_OK)


class DeletePost(APIView):
    authentication_classes = (CookieTokenAuthentication,)

    def delete(self, request, post_id, format=None):
        auth_token = request.COOKIES.get("token").split(' ')[1]

        user = Token.objects.get(key=auth_token).user
        post = Post.objects.get(id=post_id)

        if post.author == user:
            post.delete()
            return Response("Post deleted", status=status.HTTP_200_OK)

        return Response("User does not own post", status=status.HTTP_401_UNAUTHORIZED)
