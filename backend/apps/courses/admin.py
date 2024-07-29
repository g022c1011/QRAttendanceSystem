from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','start_time')
    search_fields = ('name',)
    list_filter = ('start_date','start_time',)
    ordering = ('start_date','start_time',)