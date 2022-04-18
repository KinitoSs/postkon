from django.shortcuts import get_object_or_404, render
from .models import User, Post
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'postkon_webapp/login.html')


# def show_all_users(request):
#     users = User.objects.all()
#     return render(request, 'postkon_webapp/all_users.html', context={
#         'users': users
#     })

def search_users(request, search_input):
    search_input = ""
    username_filter = User.objects.filter(username__icontains=search_input)
    first_name_filter = User.objects.filter(first_name__icontains=search_input)
    last_name_filter = User.objects.filter(last_name__icontains=search_input)
    result = username_filter.union(first_name_filter).union(last_name_filter)

def show_one_user(request, slug_user: str):
    user = get_object_or_404(User, slug=slug_user)
    posts = Post.objects.filter(user=user)
    return render(request, 'postkon_webapp/Profile.html', context={
        'user': user,
        'posts': posts,
    })

def user_settings(request, slug_user:str):
    user = get_object_or_404(User, slug=slug_user)
    return render(request, 'postkon_webapp/settings.html', context={
        'user': user,
    })

def show_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'postkon_webapp/posts.html', context={
        'posts': posts,
    })

def registration(request):
    return render(request, 'postkon_webapp/reg.html')