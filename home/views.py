from django.shortcuts import render, HttpResponse
from posts.models import Post
# Create your views here.

def index(request):

    posts = Post.objects.all().order_by('-registered_at')[:5]

    context = {
        'posts' : posts
    }

    return render(request, 'home/index.html', context)