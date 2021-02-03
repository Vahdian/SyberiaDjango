from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout as do_logout

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

def login(request):
    return render(request, "registration/login.html")

def logout(request):
    return redirect('/')