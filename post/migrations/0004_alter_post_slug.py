# Generated by Django 4.1.1 on 2022-10-21 11:04

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=builtins.id),
        ),
    ]
