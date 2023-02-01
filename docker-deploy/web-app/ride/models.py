from django.db import models

class Ride(models.Model):
    rideType = models.BooleanField()
    owner = models.IntegerField()
    ownerPassNum = models.IntegerField()
    arrivalTime = models.DateTimeField()
    dest = models.CharField(max_length=128)
    carType = models.CharField(max_length=20)
    
    specialRequest = models.CharField(blank = True, max_length=128, null = True, default=None)
    
    status = models.IntegerField(default=0)
    
    driver = models.IntegerField(blank = True, null=True, default=None)
    shared = models.JSONField(blank = True, null=True, default=None)
    def __str__(self) -> str:
        return "Ride ID: " + str(self.id) +" Ride Owner: " + str(self.owner)