from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "vault/vault.html")
        else:
            return render(request, "vault/login.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        else:
            return render(request, "vault/register.html")


def logout(request):
    if request.method == "POST":
        logout(request)
        return render(request, "vault/login.html")

@login_required
def vault(request):
    return render(request, "vault/vault.html")