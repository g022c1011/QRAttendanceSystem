from django.contrib import admin
from .models import Course, Session

class SessionInline(admin.TabularInline):
    model = Session
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time')
    search_fields = ('name',)
    list_filter = ('start_time',)
    ordering = ('start_time',)
    inlines = [SessionInline]
