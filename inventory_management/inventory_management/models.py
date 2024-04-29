from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('pclaptops', 'PC/Laptop'),
        ('vrheadset', 'VR Headset'),
        ('camsensor', 'Camera/Sensors'),
        ('pcperipheral', 'PC Peripherals'),
        ('furniture', 'Furniture'),
        ('tripod', 'Tripod'),
        ('powercable', 'Power/Cable'),
        ('vrcontroller', 'VR Controller'),
        ('other', 'Other'),
    ]

    LOCATIONS = [
        ('XRLabBlueCabinet', 'XRLab Blue Cabinet'),
        ('XRLab', 'XRLab'),
        ('XRLabBlueCabinetLarge', 'XRLab Blue Cabinet Large'),
        ('XRLabMediumWoodenCabinet', 'XRLab Medium Wooden Cabinet'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=EQUIPMENT_TYPES)
    quantity = models.IntegerField(default=1)
    audit = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, choices=LOCATIONS)
    onsite = models.BooleanField(default=False)
    
class Reservation(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()