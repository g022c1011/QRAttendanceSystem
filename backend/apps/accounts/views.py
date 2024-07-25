from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, TeacherSignUpForm, StudentSignUpForm
from django.contrib.auth.decorators import login_required

# ホーム
def home_view(request):
    return render(request, "accounts/home.html")

# サインイン
def signup_account_selection_view(request):
    if request.method == "POST":
        account_type = request.POST.get('account_type')
        if account_type in ['student']:
            request.session['account_type'] = account_type
            return redirect('accounts:student_signup')
        elif account_type in ['teacher']:
            request.session['account_type'] = account_type
            return redirect('accounts:teacher_signup')
    return render(request, "accounts/account_selection.html")

def teacher_signup_view(request):
    if request.method == "POST":
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:home")
    else:
        form = TeacherSignUpForm()
    param = {"form": form}
    return render(request, "accounts/teacher_signup.html", param)

def student_signup_view(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:home")
    else:
        form = StudentSignUpForm()
    param = {"form": form}
    return render(request, "accounts/student_signup.html", param)

# ログイン
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("accounts:userpage")
    else:
        form = LoginForm()
    param = {"form": form}
    return render(request, "accounts/login.html", param)

# ログアウト
@login_required
def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")

# ユーザーページ
@login_required
def userpage_view(request):
    return render(request, "accounts/userpage.html")


