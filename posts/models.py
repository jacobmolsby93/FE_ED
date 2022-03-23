from django.db import models
from users.models import BlogUser

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    A model for posts
    """
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name="post_author")
    slug = models.SlugField(max_length=200, unique=True)
    post_image = models.ImageField(null=True, blank=True, upload_to="media")
    post_title = models.CharField(max_length=254)
    post_body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(BlogUser, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return f"{self.post_title} - {self.slug}"

    def number_of_likes(self):
        return self.likes.count()