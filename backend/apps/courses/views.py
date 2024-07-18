from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm

# @login_required
def select_course(request):
    courses = Course.objects.all()
    return render(request, 'courses/select_course.html', {'courses': courses})

# @login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:select') 
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})
