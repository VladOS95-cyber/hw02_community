from django.http import HttpResponse
from .models import Post
from django.shortcuts import render


def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, "index.html", {"posts": latest})
