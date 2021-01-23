from django.urls import path, include
from .views import PostListView, index, logout, addComment, profile, deleteUser, deleteComments, api, terms, contact

urlpatterns = [
    path("", index),
    path("blog", PostListView.as_view()),
    path("api", api),
    path("terms", terms),
    path("logout", logout),
    path("contact",contact),
    path("profile", profile),
    path("addComment",addComment),
    path("deleteUser",deleteUser),
    path("deleteComments",deleteComments),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls")),
]