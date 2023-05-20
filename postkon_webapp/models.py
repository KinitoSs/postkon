from distutils.command.upload import upload
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    avatar_img = models.CharField(max_length=500, null=True, blank=True)
    slug = AutoSlugField(populate_from="user", unique=True)
    # slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse("one_user", args=[self.slug])

    def get_settings_url(self):
        return reverse("user_settings", args=[self.slug])

    def __str__(self):
        return f"{self.user.username}"


class Moderator(Profile):
    def delete_user_post(self, post_id):
        post = Post.objects.get(id=post_id)
        if post.profile != self:
            post.delete()


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.profile.user.username} - {self.date_uploaded}"
