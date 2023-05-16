from re import search
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Post

# Register your models here.

# admin.site.register(Profile)


# class ArticleAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}

# admin.site.register(Profile,ArticleAdmin)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)



admin.site.register(Post)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# admin.site.register(Post)
# @admin.register(Profile)
# class UserAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('user.username', )}
#     list_display = ['user.username', 'user.first_name', 'user.last_name',
#                     'birthday', 'status']
#     # list_editable = ['username', 'first_name',
#     #                  'last_name', 'birthday', 'status']
#     list_per_page = 20
#     search_field = ['user.first_name', 'user.last_name']
#     list_filter = ['user.username', 'user.first_name', 'user.last_name', 'birthday']


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['text', 'date', 'img', 'video']
#     list_editable = ['text', 'date', 'img', 'video']
#     list_per_page = 20
