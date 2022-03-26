from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from posts.models import Post

# Create your views here.


def search(request):
    """ 
    A view for searching as well as displaying search results.
    """
    query = request.GET.get('q')

    print(query)
    qs = Post.objects.all()
    if query is not None:
        searched = (
            Q(post_title__icontains=query) |
            Q(author__user__username__icontains=query)
        )
        qs = Post.objects.filter(searched)
        messages.info(request, f'Results for {query}')

    template_name = "home/search_results.html"
    context = {
        "search_list": qs,
        "query": query
    }
    return render(request, template_name, context)


def home(request):
    """
    A view to render the homepage, where all the posts from different users are going to be displayed
    """
    posts = Post.objects.all()

    template_name = "home/home.html"
    context = {
        "posts": posts
    }

    return render(request, template_name, context)