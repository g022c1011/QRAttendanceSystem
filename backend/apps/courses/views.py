from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm
from datetime import datetime, timedelta

@login_required
def select_course(request):
    #今週の授業とそれ以外と終了済み授業を分ける
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    # ログイン中の教員
    teacher = request.user

    # 教員の授業のみ表示
    this_week_courses = Course.objects.filter(
        teacher=teacher,
        start_date__range=[today, next_week]
    ).order_by('start_date', 'start_time')

    other_courses = Course.objects.filter(
        teacher=teacher,
        start_date__gt=next_week
    ).order_by('start_date', 'start_time')

    finished_courses = Course.objects.filter(
        teacher=teacher,
        start_date__lt=today
    ).order_by('start_date', 'start_time')

    context = {
        'today': today,
        'this_week_courses': this_week_courses,
        'other_courses': other_courses,
        'finished_courses': finished_courses,
    }
    
    return render(request, 'courses/select_course.html', context)

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('courses:select')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

