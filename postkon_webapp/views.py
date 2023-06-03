from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import ModelForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from matplotlib.font_manager import json_dump, json_load
from requests import Response
from turtle import update
from unicodedata import name
import json

from .forms import ProfileSettingsForm, RegisterForm, SettingsForm
from .models import Profile, Post


class Login(LoginView):
    template_name = "postkon_webapp/login.html"


class Logout(LogoutView):
    next_page = "/login"


@staff_member_required
def ban_user(request, slug_user: str):
    profile = get_object_or_404(Profile, slug=slug_user)
    profile.ban()
    return HttpResponseRedirect(reverse("one_user", args=[profile.slug]))


@csrf_exempt
def add_post(request):
    user_input = request.body.decode("utf-8")
    data = Post.add_post(request, user_input)
    return JsonResponse(data)


@csrf_exempt
def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        result = Post.delete_post(post_id)
        return JsonResponse(result)
    else:
        return JsonResponse({"success": False})


def logout_view(request):
    logout(request)
    return HttpResponse("You have been successfully logged out.")


def main_page(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    posts = Post.objects.all()
    profile = request.user.profile
    return render(
        request,
        "postkon_webapp/posts.html",
        context={
            "posts": posts,
            "profile": profile,
        },
    )


@csrf_exempt
def search_users(request):
    search_input = request.POST["user_simvol"]
    data = Profile.search_users(search_input)
    return JsonResponse(data, safe=False)


def show_one_user(request, slug_user: str):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, slug=slug_user)
        posts = Post.objects.filter(profile=profile)

        return render(
            request,
            "postkon_webapp/Profile.html",
            context={
                "profile": profile,
                "posts": posts,
            },
        )
    else:
        return redirect("/login")


@staff_member_required
def unban_user(request, slug_user: str):
    profile = get_object_or_404(Profile, slug=slug_user)
    profile.unban()
    return HttpResponseRedirect(reverse("one_user", args=[profile.slug]))


def user_settings(request, slug_user: str):
    if not request.user.is_authenticated:
        return redirect("/login")

    profile = get_object_or_404(Profile, slug=slug_user)
    if request.user.profile != profile:
        return redirect("/")

    if request.method == "POST":
        form = SettingsForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileSettingsForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect("/")
    else:
        form = SettingsForm(instance=request.user)
        profile_form = ProfileSettingsForm(instance=request.user.profile)

    return render(
        request,
        "postkon_webapp/settings.html",
        {"form": form, "profile_form": profile_form},
    )


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        birthday = form.cleaned_data.get("birthday")

        profile = Profile()
        profile.register(
            username=username,
            email=email,
            password=raw_password,
            birthday=birthday,
        )

        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect("/")
    context = {"form": form}
    return render(request, "postkon_webapp/register.html", context)