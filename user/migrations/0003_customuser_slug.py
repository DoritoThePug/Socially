# Generated by Django 4.1.1 on 2022-10-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_followers_customuser_liked_posts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=30)),
        ),
    ]
