from django.shortcuts import render

# Create your views here.
from rest_framework import permissions  # Django REST framework tools
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer

@api_view(['GET'])
def student_list_api(request):
    """
    A simple API endpoint to view all students.
    """
    # 1. Grab all student rows from your Postgres database
    students = Students.objects.all()

    # 2. Feed those rows into the translator (many=True means there's a list of them)
    serializer = StudentSerializer(students, many=True)

    # 3. Send the clean JSON data back to the browser
    return Response(serializer.data)