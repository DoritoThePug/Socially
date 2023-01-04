from django.urls import path
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token

from user import views

urlpatterns = [
    path('create-user/', csrf_exempt(views.CreateUser.as_view())),
    path('log-in/', csrf_exempt(requires_csrf_token(views.AuthenticateUser.as_view()))),
    path('logout/', views.Logout.as_view()),
    path('update-user/', views.UpdateUser.as_view()),
    path('<slug:user_slug>/', views.UserDetails.as_view()),
    path('<slug:following_user_slug>/follow/', views.FollowUser.as_view()),
]
