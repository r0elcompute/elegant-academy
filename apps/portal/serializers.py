from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'  # This tells Django to translate EVERY column (name, reg_no, email, etc.)
