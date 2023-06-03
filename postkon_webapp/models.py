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

    @classmethod
    def search_users(cls, search_input):
        users = User.objects.filter(
            models.Q(username__icontains=search_input) |
            models.Q(first_name__icontains=search_input) |
            models.Q(last_name__icontains=search_input)
        )
        data = []
        for user in users:
            data.append({
                "username": user.username,
                "url": user.profile.get_url(),
                "avatar_img": user.profile.avatar_img
            })
        return data

    def register(self, username, email, password, birthday):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        self.user = user
        self.birthday = birthday
        self.save()

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

    @classmethod
    def add_post(cls, request, user_input):
        if request.user.profile.is_banned:
            return {"error": "You are banned and can't post."}
        else:
            created_post = cls.objects.create(
                profile=request.user.profile, text=user_input
            )

            data = {
                "creator_username": created_post.profile.user.username,
                "creator_avatar_img": created_post.profile.avatar_img,
                "date_uploaded": created_post.date_uploaded,
            }

            return data

    @classmethod
    def delete_post(cls, post_id):
        post = get_object_or_404(cls, id=post_id)
        post.delete()

        return {"success": True}






# from distutils.command.upload import upload
# from django.db import models
# from django.core.validators import FileExtensionValidator
# from django.utils import timezone
# from django.utils.text import slugify
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django_extensions.db.fields import AutoSlugField


# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
#     birthday = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=255, null=True, blank=True)
#     avatar_img = models.CharField(max_length=500, null=True, blank=True)
#     slug = AutoSlugField(populate_from="user", unique=True)
#     # slug = models.SlugField(default='', null=False, db_index=True)
#     is_banned = models.BooleanField(default=False)

#     @classmethod
#     def search_users(cls, search_input):
#         username_filter = User.objects.filter(username__icontains=search_input)
#         first_name_filter = User.objects.filter(first_name__icontains=search_input)
#         last_name_filter = User.objects.filter(last_name__icontains=search_input)
#         users = username_filter.union(first_name_filter).union(last_name_filter)
#         data = []
#         for user in users:
#             username = user.username
#             avatar_img = user.profile.avatar_img
#             url = "http://127.0.0.1:8000/users/" + user.profile.slug
#             data.append({"username": username, "url": url, "avatar_img": avatar_img})
#         return data

#     def register(self, username, email, password, birthday):
#         user = User.objects.create_user(username=username, email=email, password=password)
#         self.user = user
#         self.birthday = birthday
#         self.save()

#     def ban(self):
#         self.is_banned = True
#         self.save()

#     def unban(self):
#         self.is_banned = False
#         self.save()

#     def get_url(self):
#         return reverse("one_user", args=[self.slug])

#     def get_settings_url(self):
#         return reverse("user_settings", args=[self.slug])

#     def __str__(self):
#         return f"{self.user.username}"


# class Post(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
#     date_uploaded = models.DateTimeField(default=timezone.now)
#     text = models.CharField(max_length=500)

#     @classmethod
#     def add_post(cls, request, user_input):
#         if request.user.profile.is_banned:
#             return {"error": "Ты забанен и не можешь постить."}
#         else:
#             created_post = cls.objects.create(
#                 profile=request.user.profile, text=user_input
#             )

#             data = {
#                 "creator_username": created_post.profile.user.username,
#                 "creator_avatar_img": created_post.profile.avatar_img,
#                 "date_uploaded": created_post.date_uploaded,
#             }

#             return data

#     @classmethod
#     def delete_post(cls, post_id):
#         try:
#             post = cls.objects.get(id=post_id)
#             post.delete()
#             return {"success": True}
#         except cls.DoesNotExist:
#             return {"success": False, "error": "Post not found"}

#     def __str__(self):
#         return f"{self.profile.user.username} - {self.date_uploaded}"
