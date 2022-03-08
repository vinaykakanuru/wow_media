from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    @property   
    def employees(self):
        return self.employee_set.all()

class Employee(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_joining = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
