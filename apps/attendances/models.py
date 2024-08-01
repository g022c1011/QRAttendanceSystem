from django.db import models
from apps.courses.models import Course

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendances')
    student = models.CharField(max_length=100)
    attendance_time = models.DateTimeField()
    attendance = models.CharField(max_length=10, choices=[
        ('Present', '出席'),
        ('Late', '遅刻'),
        ('Absent', '欠席'),
    ])

    def __str__(self):
        return f'{self.student} - {self.course} - {self.attendance_time} - {self.attendance}'
