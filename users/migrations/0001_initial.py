# Generated by Django 3.2.8 on 2022-03-31 22:21

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=254, null=True)),
                ('profession', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('bio', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(default='profile-placeholder', max_length=255, verbose_name='profile-image')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
