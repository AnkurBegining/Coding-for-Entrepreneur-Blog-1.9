from django.shortcuts import render, get_object_or_404
from blog.models import post

# Create your views here.

def post_list(request):
    posts = post.objects.all()
    context_data={
        'posts_list': posts
    }
    return render(request, "blog/post_list.html", context_data)


def post_create(request):
    return render(request, "blog/post_create.html", {})


def post_detail(request, id):

    instance = get_object_or_404(post, id =id)
    context_data = {
        "title" : instance.title,
        "post" : instance
    }
    return render(request, "blog/post_detail.html", context_data)


def post_update(request):
    return render(request, "blog/post_update.html", {})


def post_delete(request):
    return render(request, "blog/post_delete.html", {})
