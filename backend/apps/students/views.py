from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, "students/home.html")

@login_required
def userpage_view(request):
    return render(request, "students/userpage.html")