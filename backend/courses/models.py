from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()

    def __str__(self):
        return self.name

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.course.name} Session from {self.start_time} to {self.end_time}'
    
