from django.urls import path
from . import views

app_name = 'students_qr'

urlpatterns = [
    path('generate/', views.generate_qr, name='generate_qr'),
]
