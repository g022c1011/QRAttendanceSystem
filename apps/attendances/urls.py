from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [
    path('qr_reader/<int:course_id>/', views.qr_reader_view, name='qr_reader'),
    path('save_attendance/', views.save_attendance, name='save_attendance'),
]
