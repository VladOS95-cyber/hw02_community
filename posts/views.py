from .models import Post, Group


from django.shortcuts import render, get_object_or_404


def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    """Функция возвращает страницу сообщества
    и выводит до 12 записей на странице 
    """

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})