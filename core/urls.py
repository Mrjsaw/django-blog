from django.urls import path, include
from .views import PostListView, index, logout, addComment, profile, deleteUser, deleteComments

urlpatterns = [
    path("", index),
    path("blog", PostListView.as_view()),
    path("logout", logout),
    path("profile", profile),
    path("addComment",addComment),
    path("deleteUser",deleteUser),
    path("deleteComments",deleteComments),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls")),
]