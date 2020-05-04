from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post

# Create your views here.
def index(request) :

    posts = Post.objects.all()

    context = {
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)

def detail(request, id) :
    
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/detail.html', context)

    
