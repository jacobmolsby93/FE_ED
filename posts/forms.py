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

        def clean_field(self):
        value = self.cleaned_data['post_title']
        if len(value) => 250:
            raise django_forms.ValidationError('Only 250 characters allowed in the title')
        return value
        

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