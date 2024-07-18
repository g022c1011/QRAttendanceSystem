from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'students/login.html')

def logged_out(request):
    return render(request, 'students/logged_out.html')