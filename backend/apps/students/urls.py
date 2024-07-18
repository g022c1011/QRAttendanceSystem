from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("home/", views.home_view, name="home")
]