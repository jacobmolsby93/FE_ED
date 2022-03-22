from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BlogUser
from .forms import BlogUserForm

# Create your views here.


def profile(request):
    """
    A view to render the profile of the user
    """
    userProfile = get_object_or_404(BlogUser, user=request.user)
    if request.user.is_authenticated:
        print(request.user)

    if request.method == 'POST':
        form = BlogUserForm(request.POST, instance=userProfile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = BlogUserForm(instance=userProfile)
    # posts = profile.posts.all()

    template_name = "users/profile.html"
    context = {
        "form": form,
        "on_page": True
    }

    return render(request, template_name, context)

# def edit_profile(request):
#     """
#     Edit a product in the store
#     """
#     :
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     painting = get_object_or_404(PaintingImage, pk=painting_id)

#     if request.method == 'POST':
#         form = PaintImageForm(request.POST, request.FILES, instance=painting)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Successfully updated image!')
#             return redirect(reverse('home'))
#         else:
#             messages.error(request, 'Failed to update image. Please ensure the form is valid.')
#     else:
#         form = PaintImageForm(instance=painting)
#         messages.info(request, f'Your are editing {painting.name}')
    
#     template = 'main/edit_painting.html'
#     context = {
#         'form': form,
#         'painting': painting,
#     }

#     return render(request, template, context)