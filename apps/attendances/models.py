from django.db import models
from django.conf import settings
from apps.courses.models import Course

class Attendance(models.Model):
    # 出席ID (主キー)
    id = models.AutoField(primary_key=True)
    
    # 授業ID（coursesテーブルのID）
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendances')
    
    # 生徒ID (QRコードで読み込んだusernameを保存)
    student = models.CharField(max_length=100)

    # 出席確認時間
    attendance_time = models.DateTimeField()
    
    # 出席状況 (出席or遅刻or欠席)
    attendance = models.CharField(max_length=10, choices=[
        ('Present', '出席'),
        ('Late', '遅刻'),
        ('Absent', '欠席'),
    ])

    def __str__(self):
        return f'{self.student} - {self.course} - {self.attendance_time} - {self.attendance}'
