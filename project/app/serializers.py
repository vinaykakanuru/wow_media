from numpy import source
from rest_framework import serializers
from app.models import Department, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "date_of_joining", "location", "department",  )
        
class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ("id", "name",)