from re import search
from django.contrib import admin
from .models import User, Post

# Register your models here.

# admin.site.register(User)
admin.site.register(Post)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('username', )}
    list_display = ['username', 'first_name', 'last_name',
                    'birthday', 'status']
    # list_editable = ['username', 'first_name',
    #                  'last_name', 'birthday', 'status']
    list_per_page = 20
    search_field = ['first_name', 'last_name']
    list_filter = ['username', 'first_name', 'last_name', 'birthday']


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['text', 'date', 'img', 'video']
#     list_editable = ['text', 'date', 'img', 'video']
#     list_per_page = 20
