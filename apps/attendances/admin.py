
from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class UserAdmin(admin.ModelAdmin):
    pass