from django.db import models
from django.conf import settings

from autoslug import AutoSlugField


# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=280)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="%(class)s_liked_posts")

    class Meta:
        ordering = ('-date_created', )

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return f'/{self.author.username}/{self.id}'
