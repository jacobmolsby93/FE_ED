from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from posts.models import Post
from django.contrib.auth.decorators import login_required
from .models import BlogUser
from .forms import BlogUserForm

# Create your views here.


@login_required
def profile(request):
    """
    A view to render the profile of the user
    """
    userProfile = get_object_or_404(BlogUser, user=request.user)
    posts = Post.objects.filter(author=userProfile)
    template_name = "users/profile.html"
    context = {
        "posts": posts,
        "on_page": True,
        "userProfile": userProfile,
    }

    return render(request, template_name, context)


@login_required
def edit_profile(request):
    """
    View to edit the profile page,
    """
    profile = get_object_or_404(BlogUser, user=request.user)

    if request.method == 'POST':
        form = BlogUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('../profile')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = BlogUserForm(instance=profile)

    template_name = "users/edit_profile.html"
    context = {
        "form": form,
    }
    return render(request, template_name, context)
