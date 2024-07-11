from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Course
        fields = ['name', 'start_time']

        labels = {
            'name': '授業名',
            'start_time': '開始時間',
        }