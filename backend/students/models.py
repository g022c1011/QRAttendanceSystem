from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    google_account = models.EmailField(unique=True)

    def __str__(self):
        return self.name
