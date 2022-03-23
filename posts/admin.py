from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('post_title',)}
    list_filter = ('status', 'posted')
    list_display = ('post_title', 'slug', 'status', 'posted')
    search_fields = ['post_title', 'post_body']
    summernote_fields = ('post_body ')