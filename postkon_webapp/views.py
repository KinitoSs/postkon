from django.shortcuts import get_object_or_404, render
from .models import User, Post

# Create your views here.
# hello world

def index(request):
    return render(request, 'postkon_webapp/index.html')


def show_all_users(request):
    users = User.objects.all()
    return render(request, 'postkon_webapp/all_users.html', context={
        'users': users
    })


def show_one_user(request, slug_user: str):
    user = get_object_or_404(User, slug=slug_user)
    posts = Post.objects.filter(user=user)
    return render(request, 'postkon_webapp/one_user.html', context={
        'user': user,
        'posts': posts,
    })
