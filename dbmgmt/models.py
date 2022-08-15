from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    CustomerFirstName = models.CharField(max_length=200)
    CustomerLastName = models.CharField(max_length=200)
    CompanyName = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    CustomerEmail = models.CharField(max_length=200)
    Message = models.CharField(max_length=4096)
    Timestamp = models.DateTimeField(auto_now=True)
    @property
    def __str__(self):
        return self.Name
class EmployeeContact(models.Model):
    EmployeeName = models.CharField(max_length=200)
    EmployeeEmail = models.CharField(max_length=200)
    def __str__(self):
        return self.EmployeeName