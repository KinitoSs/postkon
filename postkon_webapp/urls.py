from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('posts/', views.main_page, name='all_posts'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('users/<slug:slug_user>/', views.show_one_user, name='one_user'),
    path('users/<slug:slug_user>/settings',
         views.user_settings, name='user_settings'),
    path('register/', views.register_view, name='register'),
]
