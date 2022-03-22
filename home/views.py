from django.shortcuts import render

# Create your views here.


def home(request):
    """
    A view to render the homepage, where all the posts from different users are going to be displayed
    """

    template_name = "home/home.html"
    context = {}

    return render(request, template_name, context)