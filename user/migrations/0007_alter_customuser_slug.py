# Generated by Django 4.1.1 on 2022-10-27 16:57

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_customuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='username', unique=True),
        ),
    ]
