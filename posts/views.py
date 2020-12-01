from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    """Функция возвращает страницу сообщества
    и выводит до 12 записей на странице
    """

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})
