from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


# Create your views here.


class CreatePost(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        auth_token = request.headers.get('Authorization').split(' ')[1]

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
    def get(self, request, format=None):
        users = get_user_model()

        try:
            user = users.objects.get(email=request.GET['email'])
            posts = Post.objects.filter(author=user)

            serializer = PostSerializer(posts, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except users.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)


class PostDetail(APIView):
    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, post_id, format=None):
        post = self.get_object(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikePost(APIView):
    permission_classes = (IsAuthenticated, )

    def patch(self, request, post_id, format=None):
        auth_token = request.headers.get('Authorization').split(' ')[1]

        user = Token.objects.get(key=auth_token).user

        post = Post.objects.get(id=post_id)

        if user in post.likes.all():
            post.likes.remove(user)
            user.liked_posts.remove(post)
        else:
            post.likes.add(user)
            user.liked_posts.add(post)

        post.save()
        user.save()

        return Response("Success", status=status.HTTP_200_OK)

    def get(self, request, post_id, format=None):
        auth_token = request.headers.get('Authorization').split(' ')[1]

        post = Post.objects.get(id=post_id)
        user = Token.objects.get(key=auth_token).user

        if user in post.likes.all():
            return Response("Post liked", status=status.HTTP_200_OK)
        else:
            return Response("Post not liked", status=status.HTTP_200_OK)


class DeletePost(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, post_id, format=None):
        auth_token = request.headers.get("Authorization").split(' ')[1]

        user = Token.objects.get(key=auth_token).user
        post = Post.objects.get(id=post_id)

        if post.author == user:
            post.delete()
            return Response("Post deleted", status=status.HTTP_200_OK)
        else:
            return Response("User does not own post", status=status.HTTP_401_UNAUTHORIZED)
