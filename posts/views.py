from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import json
from .models import Post

# Create your views here.
def index(request) :

    posts = Post.objects.all()

    context = {
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)

def detail(request, id) :
    if(request.method == 'POST') :
        return update(request, id)
    post = get_object_or_404(Post, id=id)

    content = json.dumps(post.content)

    return render(request, 'posts/detail.html', {
        'post': post,
        'content': content
    })

def edit(request, id) :

    post =  get_object_or_404(Post, id=id)

    return render(request, 'posts/edit.html', { 'post': post, 'content': json.dumps(post.content)  })

def update(request, id) :
    body = request.POST

    post = get_object_or_404(Post, id=id)
    post.title = body['title']
    post.subtitle = body['subtitle']
    post.content = body['content']
    post.save();

    return redirect('posts:edit', id=id)