from django.urls import path, include
from .views import PostListView, index, logout, addComment, profile

urlpatterns = [
    path("", index),
    path("blog", PostListView.as_view()),
    path("logout", logout),
    path("profile", profile),
    path("addComment",addComment),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls")),
]