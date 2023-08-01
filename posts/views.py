from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment


def index(request):
    return HttpResponse('welcome to django')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'posts/post_details.html', context=context)
