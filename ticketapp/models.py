from django.db import models

# Create your models here.
class Bus(models.Model):
    operator=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    coach1=models.CharField(max_length=10)
    seats=models.DecimalField(max_digits=2, decimal_places=0)
    route=models.CharField(max_length=100)
    boarding=models.CharField(max_length=100)
    dropping=models.CharField(max_length=100)

class Details(models.Model):
    coaches=[('','Select Coach'),('ACE','AC Economy'),('ACB','AC Business Class'),('NAC','Non AC')]
    Boarding=models.CharField(max_length=100)
    Destination=models.CharField(max_length=100)
    Date=models.DateField()
    Coach=models.CharField(max_length=10, choices=coaches)

class ContactInfo(models.Model):
    name=models.CharField(max_length=100)
    phone=models.DecimalField(max_digits=11, decimal_places=0)
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=500)

class ReserveInfo(models.Model):
    seats=[('','Select Seats'),(27,'27 Seats'),(28,'28 Seats'),(34,'34 Seats'),(36,'36 Seats'),(40,'40 Seats')]
    type=[('','Select Coach'),('ACE','AC Economy'),('ACB','AC Business Class'),('NAC','Non AC')]
    journey_date=models.DateField()
    return_date=models.DateField()
    boarding=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    pref_bus=models.CharField(max_length=100)
    no_of_bus=models.CharField(max_length=100, choices=type)
    no_of_seat=models.CharField(max_length=30, choices=seats)
    name=models.CharField(max_length=100)
    phone=models.DecimalField(max_digits=11, decimal_places=0)
    address=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)