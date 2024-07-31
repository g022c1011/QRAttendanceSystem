from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('select/', views.select_course, name='select'),
    path('create/', views.create_course, name='create'),
]
