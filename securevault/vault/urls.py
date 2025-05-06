from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("register_view", views.register_view, name="register_view"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("vault", views.vault, name="vault")


]