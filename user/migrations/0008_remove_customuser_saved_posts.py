# Generated by Django 4.1.1 on 2022-10-28 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_customuser_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='saved_posts',
        ),
    ]