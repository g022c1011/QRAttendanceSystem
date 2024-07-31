from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
import re

class TeacherSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.account_type = 'teacher'
        if commit:
            user.save()
        return user

class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        pattern = r'^G\d{3}C\d{4}$'
        if not re.match(pattern, username):
            raise forms.ValidationError("学籍番号は GXXXCXXXX の形式で入力してください。")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith('@g.neec.ac.jp'):
            raise forms.ValidationError("メールアドレスは @g.neec.ac.jp の形式で入力してください。")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.account_type = 'student'
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def non_field_errors(self):
        errors = super().non_field_errors()
        return errors