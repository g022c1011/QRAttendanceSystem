from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:home")
    else:
        form = SignUpForm()
    param = {"form": form}
    return render(request, "accounts/signup.html", param)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("accounts:userpage")
    else:
        form = LoginForm()
    param = {"form": form}
    return render(request, "accounts/login.html", param)

@login_required
def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")

def home_view(request):
    return render(request, "accounts/home.html")

@login_required
def userpage_view(request):
    return render(request, "accounts/userpage.html")