from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list_api, name='student-list-api'),
]