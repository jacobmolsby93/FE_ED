from .models import Comment 
from django import forms 


class CommentForm(forms.ModelForm):
    """
    Model form for comments
    """
    class Meta:
        model = Comment
        # The trailing comma is for python not to read it as a string instead
        # of a tupple
        fields = ('comment_content',)