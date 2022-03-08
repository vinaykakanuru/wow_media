from django.shortcuts import render
from rest_framework import viewsets

from app.models import Department, Employee
from app.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    
