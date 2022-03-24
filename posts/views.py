from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from users.models import BlogUser
# Create your views here.




def post_detail(request, slug):
    """
    View for viewing a specific post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    template_name = "posts/post_detail.html"
    context = {
        "post": post,
        "liked": liked,
    }
    return render(request, template_name, context)


def like(request, slug):
    """
    Function to post a like by user.
    """

    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

