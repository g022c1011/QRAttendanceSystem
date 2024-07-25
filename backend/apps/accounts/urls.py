from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("home/", views.home_view, name="home"),

    path("signup_account_selection/", views.signup_account_selection_view, name="signup_account_selection"),

    path("teacher_signup/", views.teacher_signup_view, name="teacher_signup"),
    path("student_signup/", views.student_signup_view, name="student_signup"),

    path("login/", views.login_view, name="login"),

    path("userpage/", views.userpage_view, name="userpage"),

    path("logout/", views.logout_view, name="logout"),

]