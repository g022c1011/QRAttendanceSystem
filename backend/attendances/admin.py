from django.contrib import admin
from .models import Attendance

admin.site.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'attendance_time')
    search_fields = ('student__name', 'course__name')
    list_filter = ('course', 'attendance_time')
    ordering = ('-attendance_time',)
