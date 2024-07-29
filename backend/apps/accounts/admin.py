from django.contrib import admin
from .models import User 

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','account_type')
    search_fields = ('username',)
    list_filter = ('account_type',)
    ordering = ('account_type',)