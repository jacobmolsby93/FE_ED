from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class BlogUser(models.Model):
    """
    A model for the user to update profile information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    profession = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField()
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        BlogUser.objects.create(user=instance)
    # Existing users: just save the profile
    instance.bloguser.save()
