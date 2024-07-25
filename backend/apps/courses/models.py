from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    start_time = models.TimeField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    def __str__(self):
        return self.name

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.course.name} Session from {self.start_time} to {self.end_time}'
    
