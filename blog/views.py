from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Post


def index(request):
    posts = get_list_or_404(Post)

    return render(request, template_name='blog/index.html', context={
        'posts': posts
    })


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, template_name='blog/post_detail.html', context={
        'post': post
    })


def about(request):
    return render(request, template_name='blog/about.html')
