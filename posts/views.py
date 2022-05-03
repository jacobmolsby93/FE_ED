from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import BlogUser
from posts.models import Post, Comment
from django.contrib import messages
from .forms import CommentForm, PostForm
# Create your views here.


def edit_post(request, slug):
    """
    Edit a post from user profile page.
    """
    post = get_object_or_404(Post, slug=slug)
    user = BlogUser.objects.all()
    blog_user = get_object_or_404(user, user=request.user)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.instance.author = blog_user
            post_form.instance.status = 1
            post_form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to update post. Check image type.')
    else:
        post_form = PostForm(instance=post)
        messages.info(request, f'Your are editing {post.post_title}')
    template_name = 'posts/edit_post.html'
    context = {
        'post': post,
        'post_form': post_form,
    }

    return render(request, template_name, context)


def delete_post(request, slug):
    """
    Delete post
    """

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'post deleted!')
    return redirect(reverse('profile'))


def add_post(request):
    """
    View for adding posts
    """
    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry you need to be logged in to add a post.")
        return redirect(reverse('account_login'))
    if request.method == "POST":
        user = BlogUser.objects.all()
        blog_user = get_object_or_404(user, user=request.user)
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save(commit=False)
            post_form.instance.author = blog_user
            post_form.instance.status = 1
            post_form.save()
            messages.success(request, "Succesfully posted")
            return redirect(reverse('profile'))
        else:
            messages.error(
                request,
                "Failed to add post. Make sure you'r \
                    image is the right format.")
    else:
        post_form = PostForm()
    template_name = 'posts/add_post.html'
    context = {
        "post_form": post_form
    }
    return render(request, template_name, context)


@login_required
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
        messages.success(request, f'You left a comment on {post.post_title}')
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


def delete_comment(request, id, slug):
    """
    View for deleting comment
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=id)
    user = BlogUser.objects.all()
    blog_user = get_object_or_404(user, user=request.user)
    if blog_user == comment.comment_author:
        comment.delete()
        messages.success(request, 'comment deleted!')
        return redirect(reverse('post_detail', args=[slug]))
    else:
        messages.error(request, "Only comment author can delete")
        return redirect(reverse('post_detail', args=[slug]))
