from django.urls import path
from .views import index, login, logged_out

urlpatterns = [
    path('/', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logged_out, name='logged_out'),
]