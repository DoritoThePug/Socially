from django.contrib.auth import authenticate, login
from django.template.defaultfilters import slugify
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.


class CreateUser(APIView):
    def post(self, request, format=None):
        user = CustomUser.objects.create_user(
            email=request.data["email"],
            password=request.data["password"],
            username=request.data["username"],
            profile_picture=request.data["profile_picture"],
            bio=request.data["bio"],
            slug=slugify(request.data["slug"])
        )

        return Response("Creation successful")


class AuthenticateUser(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password = request.data["password"]

        print(email, password)

        user = authenticate(email=email, password=password)

        print(user)

        if user is not None:
            login(request, user)

            auth_token, created = Token.objects.get_or_create(user=user)

            serializer = UserSerializer(user)

            return Response({'token': auth_token.key, 'user': serializer.data})
        else:
            return Response("Error")


class UserDetails(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, user_slug, format=None):
        try:
            user = CustomUser.objects.all().get(slug=user_slug)

            serializer = UserSerializer(user)

            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response("User does not exist")


class FollowUser(APIView):
    permission_classes = (IsAuthenticated, )

    def patch(self, request, following_user_slug, format=None):
        auth_user = request.headers["Authorization"].split()[1]

        user = Token.objects.get(key=auth_user).user # User trying to follow

        try:
            following_user = CustomUser.objects.get(slug=following_user_slug) # User being followed

            if user in following_user.followers.all():
                following_user.followers.remove(user)
                user.following.remove(following_user)
            else:
                following_user.followers.add(user)
                user.following.add(following_user)

            user.save()
            following_user.save()

            serializer = UserSerializer(following_user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
