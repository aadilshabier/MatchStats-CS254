from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path("login/",
        auth_views.LoginView.as_view(template_name="user/login.html", next_page="main:index"),
        name="login"),
    path("logout/",
        auth_views.LogoutView.as_view(next_page="main:index"),
        name="logout"),
]