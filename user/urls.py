from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from user import views

urlpatterns = [
    path('create-user/', views.CreateUser.as_view()),
    path('log-in/', csrf_exempt(views.AuthenticateUser.as_view())),
    path('hammy/', views.Test.as_view()),
    path('<slug:user_slug>/', views.UserDetails.as_view()),
    path('<slug:following_user_slug>/follow/', views.FollowUser.as_view()),

]
