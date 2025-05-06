from django.urls import path

from . import views

urlpatterns = [

    path("vault/", views.vault, name="vault"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout")


]