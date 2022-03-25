from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from users.models import BlogUser
from posts.models import Post
from django.contrib import messages
from .forms import CommentForm, PostForm
# Create your views here.


def add_post(request):
    """
    View for adding posts
    """
    if not request.user.is_authenticated:
        messages.error(request, "Sorry you need to be logged in to add a post.")
        return redirect(reverse('account_login'))
    
    if request.method == "POST":
        user = BlogUser.objects.all()    
        blog_user = get_object_or_404(user, user=request.user)
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.instance.author = blog_user
            post_form.instance.status = 1
            post_form.save()
            messages.success(request, "Succesfully posted")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Failed to add post. Make sure you'r image is the right format.")
    else:
        post_form = PostForm()
    template_name = 'posts/add_post.html'
    context = {
        "post_form": post_form
    }
    return render(request, template_name, context)


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




