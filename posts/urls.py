from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name="add_post"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('like/<slug:slug>/', views.like, name="like"),
    path('edit_post/<slug:slug>/', views.edit_post, name="edit_post"),
    path('delete/<slug:slug>/', views.delete_post, name="delete"),
    path(
        'delete_comment/<int:id>/<slug:slug>/',
        views.delete_comment, name="delete_comment"),
]
