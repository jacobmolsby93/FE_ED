from .models import Comment, Post
from django import forms 


class PostForm(forms.ModelForm):
    """
    Form to add post
    """ 
    class Meta:
        """
        Specifying what fields should be editable in the form.
        """
        model = Post
        fields = ('post_image', 'post_title', 'post_body',)
        

class CommentForm(forms.ModelForm):
    """
    Model form for comments
    """
    class Meta:
        """
        Specifying what fields should be editable in the form.
        """
        model = Comment
        # The trailing comma is for python not to read it as a string instead
        # of a tupple
        fields = ('comment_content',)