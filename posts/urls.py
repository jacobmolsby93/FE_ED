from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/<str:author>/', views.PostDetail.as_view(), name='post_detail')
]