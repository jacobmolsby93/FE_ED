from django.shortcuts import render, redirect
from posts.models import Post
from users.models import BlogUser
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def search(request):
    """ 
    A view for searching as well as displaying search results.
    """
    if request.method == "POST":
        searched = request.POST["searched"]
        authors = BlogUser.objects.filter(post_author__contains=searched)
        template_name = "home/search_results.html"
        context = {
            "searched": searched,
            "authors": authors,
        }
        return render(request, template_name, context)
    else:
        messages.error(request, "We're sorry, we did not find anything matching your search!")
        return redirect('home')


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