# Generated by Django 3.2.8 on 2022-03-31 22:21

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('post_image', cloudinary.models.CloudinaryField(default='post-placeholder', max_length=255, verbose_name='post-image')),
                ('post_title', models.CharField(max_length=254)),
                ('post_body', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='users.bloguser')),
                ('likes', models.ManyToManyField(blank=True, related_name='blog_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='users.bloguser')),
                ('likes', models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
            ],
            options={
                'ordering': ['posted'],
            },
        ),
    ]
