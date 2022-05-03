from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_filter = ('status', 'posted')
    list_display = ('post_title', 'slug', 'status', 'posted')
    search_fields = ['post_title', 'post_body']
    summernote_fields = ('post_body ')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_content', 'posted')
    list_filter = ('posted',)
    search_fields = ['name', 'comment_content']
