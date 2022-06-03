from turtle import update
from unicodedata import name
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from matplotlib.font_manager import json_dump, json_load
from requests import Response
from .models import Profile, Post
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from postkon_webapp.forms import ProfileSettingsForm, RegisterForm, SettingsForm
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class Login(LoginView):
    template_name = 'postkon_webapp/login.html'

class Logout(LogoutView):
    next_page = '/login'  # Редирект на страницу логина

def main_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        profile = request.user.profile
        return render(request, 'postkon_webapp/posts.html', context={
            'posts': posts,
            'profile': profile,
        })
    else:
        return redirect('/login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            birthday = form.cleaned_data.get('birthday')
            Profile.objects.create(
                user=user,
                birthday=birthday,
            )
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'postkon_webapp/register.html', {'form': form})

@csrf_exempt
def search_users(request):
    search_input = request.POST['user_simvol']
    username_filter = User.objects.filter(username__icontains=search_input)
    first_name_filter = User.objects.filter(first_name__icontains=search_input)
    last_name_filter = User.objects.filter(last_name__icontains=search_input)
    users = username_filter.union(first_name_filter).union(last_name_filter)
    data = []
    for user in users:
        username = user.username
        avatar_img = user.profile.avatar_img
        url = 'http://127.0.0.1:8000/users/' + user.profile.slug
        data.append({
            "username": username,
            "url": url,
            "avatar_img": avatar_img
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_post(request):

    user_input = request.body.decode('utf-8')

    created_post = Post.objects.create(
        profile=request.user.profile,
        text=user_input
    )
    
    data = {
        "creator_username": created_post.profile.user.username,
        "creator_avatar_img": created_post.profile.avatar_img,
        "date_uploaded": created_post.date_uploaded
    }

    return JsonResponse(data)

def show_one_user(request, slug_user: str):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, slug=slug_user)
        posts = Post.objects.filter(profile=profile)
    
        return render(request, 'postkon_webapp/Profile.html', context={
            'profile': profile,
            'posts': posts,
        })
    else:
        return redirect('/login')

def user_settings(request, slug_user: str):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, slug=slug_user)
        if request.user.profile == profile:
            if request.method == 'POST':
                form = SettingsForm(request.POST, request.FILES, instance=request.user)
                profile_form = ProfileSettingsForm(request.POST, request.FILES, instance=request.user.profile)
                if form.is_valid() and profile_form.is_valid():
                    form.save()
                    profile_form.save()
                    return redirect('/')
            else:
                form = SettingsForm(instance=request.user)
                profile_form = ProfileSettingsForm(instance=request.user.profile)

            return render(request, 'postkon_webapp/settings.html', {'form': form, 'profile_form': profile_form})
        else:
            return redirect('/')
    else:
        return redirect('/login')

def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из учетной записи')
