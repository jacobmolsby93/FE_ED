from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('like/<slug:slug>/', views.like, name="like"),
    path('add_post', views.add_post, name="add_post"),
]