from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'google_account')
    search_fields = ('name', 'student_id')
    list_filter = ('google_account',)
    ordering = ('student_id',)
