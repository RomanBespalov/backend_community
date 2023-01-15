from django.shortcuts import render, get_object_or_404

from .models import Post, Group

n = 10  # Константа для количества постов на странице


def index(request):
    posts = Post.objects.all()[:n]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
