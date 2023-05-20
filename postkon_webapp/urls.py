from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("users/<slug:slug_user>/", views.show_one_user, name="one_user"),
    path("users/<slug:slug_user>/settings", views.user_settings, name="user_settings"),
    path("register/", views.register_view, name="register"),
    path("search-user/", views.search_users, name="search_users"),
    path("delete_post/", views.delete_post, name="delete_post"),
    path("add-post/", views.add_post, name="add_post"),
]
