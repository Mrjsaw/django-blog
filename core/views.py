from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponseRedirect
import html
# Create your views here.

def index(request):
    user = request.user
    if user.is_authenticated and user.email_verified:
        return redirect("/blog")        
    else:
        print(request)
        return render(request, "index.html")

def logout(request):
    log_out(request)
    return_to = urlencode({"returnTo": request.build_absolute_uri("/")})
    logout_url = "https://{}/v2/logout?client_id={}&{}".format(
        settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to,
    )

    return HttpResponseRedirect(logout_url)


def addComment(request):
    #Escape input 
    escaped_id = html.escape(request.POST.get('post_id'))
    post = get_object_or_404(Post, id= escaped_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= post
            comment.name = request.user.username
            comment.save()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return HttpResponseRedirect('/')
   
class PostListView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        posts = Post.objects.all()
        comments = Comment.objects.all()
        context = {"posts": posts, "comments": comments}
        return render(request, "base.html", context)

