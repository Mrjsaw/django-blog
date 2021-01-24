from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View
from django.utils.decorators import method_decorator
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.views.decorators.http import require_http_methods
import html

# inheritance custom 401
class Http401(HttpResponse):
    def __init__(self):
        super().__init__('401 Unauthorized', status=401)

   
# Create your views here.

def contact(request):
    return render(request, "contact.html")

def terms(request):
    return render(request, "terms.html")

def api(request):
    return render(request,"api.html")

#post request that deletes all comments and user information
@require_http_methods(["POST"])
def deleteUser(request):
    user = request.user
    if user.is_authenticated:
        user.delete()
        return render(request, "index.html")
    return HttpResponseForbidden()

#post request to delete all comments made by this user
@require_http_methods(["POST"])
def deleteComments(request):
    user = request.user
    if user.is_authenticated:
        for comment in Comment.objects.all():
            if comment.name == user:
                comment.delete()
        return render(request, "profile.html", {"user":user,"comments":[comment for comment in Comment.objects.all() if comment.name == user]})
    return HttpResponseForbidden()

def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/blog")        
    else:
        return render(request, "index.html")

def logout(request):
    #custom logout for admin accounts when testing in dev-mode:
    #if request.user.is_staff:
    #    log_out(request)
    #    return render(request, "index.html")
    
    #auth0 logout
    log_out(request)
    return_to = urlencode({"returnTo": request.build_absolute_uri("/")})
    logout_url = "https://{}/v2/logout?client_id={}&{}".format(
        settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to,
    )

    return HttpResponseRedirect(logout_url)

@login_required
def profile(request):
    user = request.user  
    if user.is_authenticated:
        comments = [comment for comment in Comment.objects.all() if comment.name == request.user]
        context = {"user": user, "comments":comments}
        return render(request, "profile.html",context)
    return HttpResponseForbidden()


def addComment(request):
    #Escape input 
    escaped_id = html.escape(request.POST.get('post_id'))
    post = get_object_or_404(Post, id= escaped_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= post
            comment.name = request.user
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
        posts_count = {}
        for x in posts:
            ctr = 0
            for y in comments:
                if y.post_id == x.id:
                    ctr+=1
            posts_count[x.id] = ctr
        context = {"posts": posts, "comments": comments,"posts_count":posts_count}
        return render(request, "base.html", context)
