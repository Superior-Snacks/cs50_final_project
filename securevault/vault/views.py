from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login():
    ...

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "vault.register.html")

def logout():
    ...