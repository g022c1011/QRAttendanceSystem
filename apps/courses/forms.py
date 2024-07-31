from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Course
        fields = ['name','start_date', 'start_time']

        labels = {
            'name': '授業名',
            'start_date': '開始日時',
            'start_time': '開始時間',
        }