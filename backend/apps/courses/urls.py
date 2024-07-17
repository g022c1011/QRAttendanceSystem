from django.urls import path
from .views import select_course, create_course

urlpatterns = [
    path('select/', select_course, name='select_course'),
    path('create/', create_course, name='create_course'),
]
