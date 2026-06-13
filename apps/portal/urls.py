from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='portal'),
    path('students/', views.student_list_api, name='student-list-api'),
]