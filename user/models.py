from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from autoslug import AutoSlugField

from post.models import Post

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        #
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        user = self.create_user(email=email, password=password,
                                username=username, is_superuser=True, **extra_fields)
        user.is_admin = True
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(
        max_length=30, null=False, blank=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(
        upload_to='uploads/', default="default-user-image.png", blank=False, null=False)
    bio = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_admin = models.BooleanField(default=False)
    liked_posts = models.ManyToManyField(
        Post, blank=True, related_name="%(class)s_liked_posts")
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)
    slug = AutoSlugField(populate_from='username',
                         unique=True, blank=False, null=False)

    @property
    def is_staff(self):
        return self.is_admin

    def get_profile_picture(self):
        return 'https://192.168.88.123:8000' + self.profile_picture.url

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
