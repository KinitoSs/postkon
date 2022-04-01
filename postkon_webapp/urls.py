from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('users/', views.show_all_users, name='all_users'),
    path('users/<slug:slug_user>/', views.show_one_user, name='one_user'),
]
