from django.urls import path

from post import views

urlpatterns = [
    path('post/', views.CreatePost.as_view()),
    path('latest-posts/', views.LatestPosts.as_view()),
    path('posts/<slug:user_slug>/', views.GetUserPosts.as_view()),
    path('posts/<slug:user_slug>/<int:post_id>/', views.PostDetail.as_view()),
    path('posts/<int:post_id>/like/', views.LikePost.as_view()),
    path('posts/<int:post_id>/delete/', views.DeletePost.as_view()),
]
