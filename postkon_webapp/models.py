from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.shortcuts import get_object_or_404


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    avatar_img = models.CharField(max_length=500, null=True, blank=True)
    slug = AutoSlugField(populate_from="user", unique=True)
    is_banned = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

    def add_post(self, user_input):
        if self.is_banned:
            return {"error": "You are banned and can't post."}
        else:
            created_post = self.post_set.create(text=user_input)

            data = {
                "creator_username": self.user.username,
                "creator_avatar_img": self.avatar_img,
                "date_uploaded": created_post.date_uploaded,
            }

            return data

    def delete_post(self, post_id):
        post = get_object_or_404(self.post_set, id=post_id)
        post.delete()

        return {"success": True}

    @classmethod
    def search_users(cls, search_input):
        users = User.objects.filter(
            models.Q(username__icontains=search_input)
            | models.Q(first_name__icontains=search_input)
            | models.Q(last_name__icontains=search_input)
        )
        data = []
        for user in users:
            data.append(
                {
                    "username": user.username,
                    "url": user.profile.get_url(),
                    "avatar_img": user.profile.avatar_img,
                }
            )
        return data

    @staticmethod
    def register(username, email, password, birthday):
        user = User.objects.create_user(
            username=username, email=email, password=password
        )

        profile = Profile(user=user, birthday=birthday)
        profile.save()

        return profile

    def ban(self):
        self.is_banned = True
        self.save()

    def unban(self):
        self.is_banned = False
        self.save()

    def get_url(self):
        return reverse_lazy("one_user", args=[self.slug])

    def get_settings_url(self):
        return reverse_lazy("user_settings", args=[self.slug])

    @property
    def is_admin(self):
        return self.user.is_superuser


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.profile.user.username} - {self.date_uploaded}"
