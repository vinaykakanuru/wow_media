from django.urls import path, include
from app.views import EmployeeViewset, DepartmentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset, basename="employee")
router.register('department', DepartmentViewset, basename="department")

urlpatterns = [
    path('', include(router.urls)),
]