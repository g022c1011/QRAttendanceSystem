from django.db import models
from apps.courses.models import Course
from apps.students.models import Student

class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field='student_id', db_column='student_id')
    attendance_time = models.DateTimeField()

    def __str__(self):
        return f'{self.student.name} - {self.course.name}'
