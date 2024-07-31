from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('teacher', '教師'),
        ('student', '生徒'),
    ]

    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='student')
