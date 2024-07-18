from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from .forms import LoginForm, SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:home")
    else:
        form = SignUpForm()
    param = {"form": form}
    return render(request, "accounts/signup.html", param)