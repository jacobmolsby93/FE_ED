from django.shortcuts import render
from posts.models import Post

# Create your views here.


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