from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
# Create your views here.


class PostDetail(View):
    """
    Class based view for displaying the post detail
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
            }
        )
