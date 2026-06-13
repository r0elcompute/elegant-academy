from django.contrib import admin
from .models import Students, Teachers, Courses, Enrollments, Grades, Fees, Classes, Departments, Attendance

admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Enrollments)
admin.site.register(Grades)
admin.site.register(Fees)
admin.site.register(Classes)
admin.site.register(Departments)
admin.site.register(Attendance)
admin.site.register(Teachers)