
from django.db import models


# Create your models here.

class Booking(models.Model):
    SNo = models.AutoField(primary_key=True)
    BookingDate = models.DateField()
    EmployeeName = models.CharField(max_length=100)
    SAP_Code = models.CharField(max_length=8)
    ContactNo = models.CharField(max_length=10)
    VehicleType = models.CharField()
    PickupLocation = models.CharField(max_length=100)
    PickupTime = models.TimeField()
    Purpose = models.CharField(max_length=100)
    DropLocation = models.CharField(max_length=100)
    Stops = models.CharField(max_length=100)
    ReturnTime = models.TimeField()
    DropLocation = models.CharField(max_length=100)
    AccompanyingPerson = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.Em}"