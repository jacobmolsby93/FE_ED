# Generated by Django 3.2.8 on 2022-04-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_bloguser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
