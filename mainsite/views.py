from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No. %d, %s <br>" %(count, post))
        post_lists.append('<small>' + post.body + '</small><br><hr>')
    return HttpResponse(post_lists)
