from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from users.models import BlogUser
from cloudinary.models import CloudinaryField

from .utils import slugify_instance_title


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    A model for posts
    """
    author = models.ForeignKey(
        BlogUser, on_delete=models.CASCADE, related_name="post_author")
    slug = models.SlugField(blank=True, null=True)
    post_image = CloudinaryField('post_image', default="placeholder")
    post_title = models.CharField(max_length=254)
    post_body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Meta class to order the posts, As latest displaying first.
        """
        ordering = ['-posted']

    def __str__(self):
        return f"{self.post_title} - {self.slug}"

    def number_of_likes(self):
        """
        Model function to count the number of likes that the post has.
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        if self.slug is None:
            slugify_instance_title(self, save=False)
        super().save(*args, **kwargs)


def user_post_save(sender, instance, created, *args, **kwargs):
    """
    Saves the slug with a random number after the post has been created.
    """
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(user_post_save, sender=Post)


class Comment(models.Model):
    """
    Model for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name="comment_author")
    comment_content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='comment_likes', blank=True)

    class Meta:
        ordering = ['posted']

    def number_of_likes(self):
        """
        Model function to count the number of likes that the post has.
        """
        return self.likes.count()

    def __str__(self):
        return f"{self.comment_author}"
