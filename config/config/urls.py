from django.contrib import admin
from django.urls import path
from main import views

urlspatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),
]