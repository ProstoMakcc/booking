from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import ExtendedUser

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("room-list")
    else:
        form = LoginForm()

    return render(request, "auth_system/login.html", {"form": form})

def logout_view(request):
    logout(request)

    return redirect("room-list")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import ExtendedUser

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            email = form.cleaned_data["email"]

            if password == confirm_password:
                ExtendedUser.objects.create_user(username=username, email=email, password=password)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("room-list")
                else:
                    messages.error(request, "Authentication failed. Please try again.")
            else:
                messages.warning(request, "Passwords do not match.")
        else:
            messages.error(request, "Form is not valid. Please correct the errors.")
    else:
        form = RegisterForm()

    return render(request, "auth_system/register.html", {"form": form})
            

