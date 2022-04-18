from distutils.command.upload import upload
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    birthday = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    avatar_img = models.ImageField(upload_to='images_uploaded', null=True)
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse('one_user', args=[self.slug])

    def get_settings_url(self):
        return reverse('user_settings', args=[self.slug])

    def __str__(self):
        return f'{self.username}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    text = models.CharField(max_length=500)
    img = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return f'{self.user.username} - {self.date_uploaded}'
