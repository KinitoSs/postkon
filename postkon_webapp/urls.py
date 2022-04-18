from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('users/<slug:slug_user>/', views.show_one_user, name='one_user'),
    path('users/<slug:slug_user>/settings', views.user_settings, name='user_settings'),
    path('posts/', views.show_all_posts, name='all_posts'),
    path('registration/', views.registration, name='registration'),
]
