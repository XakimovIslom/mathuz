from django.shortcuts import render
from .models import Post, Category, Tag, About
from django.db.models import Q


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    category = request.GET.get('category')
    if category:
        posts = Post.objects.filter(category__title__exact=category)

    tag = request.GET.get('tag')
    if tag:
        posts = Post.objects.filter(tag__title__exact=tag)

    q = request.GET.get('q')
    if q:
        posts = Post.objects.filter(Q(title__icontains=q) |
                                    Q(content__icontains=q)
                                    )

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'q': q,
    }
    return render(request, 'main.html', context)


def about_me(request):
    abouts = About.objects.all()
    
    context = {
        'abouts': abouts
    }
    return render(request, 'about.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "post": post,
        "categories": categories,
        "tags": tags,
    }
    return render(request, 'post_detail.html', context)
