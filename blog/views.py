from django.shortcuts import render, get_object_or_404
from blog.models import post
from blog.forms import PostForm

# Create your views here.

def post_list(request):
    posts = post.objects.all()
    context_data={
        'posts_list': posts
    }
    return render(request, "blog/post_list.html", context_data)


def post_create(request):
    form = PostForm(request.POST)

    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()

    context ={
        'form': form
    }
    return render(request, "blog/post_create.html", context)


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
