from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    google_account = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field='student_id', db_column='student_id')
    attendance_time = models.DateTimeField()

    def __str__(self):
        return f'{self.student.name} - {self.course.name}'

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.course.name} Session from {self.start_time} to {self.end_time}'
