from django.shortcuts import render, get_object_or_404, reverse
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from .models import Post, Comment
from users.models import BlogUser
from django.contrib.auth.models import User
from .forms import CommentForm
# Create your views here.


def post_detail(request, slug):
    """
    View for viewing a specific post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-posted")
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    user = BlogUser.objects.all()    
    blog_user = get_object_or_404(user, user=request.user)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.comment_author = blog_user
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = CommentForm()

    template_name = "posts/post_detail.html"
    context = {
        "comments": comments,
        "comment_form": comment_form,
        "post": post,
        "liked": liked,
    }
    return render(request, template_name, context)


def like(request, slug):
    """
    Function to lika a post.
    """

    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def like_comment(request, slug, id):
    """
    Function to lika a post.
    """

    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=id)
    if post.comment.likes.filter(id=request.user.id).exists():
        post.comment.likes.remove(request.user)
    else:
        post.comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))



