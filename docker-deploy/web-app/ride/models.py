from django.db import models
from rideSharing.models import User

class Ride(models.Model):
    rideType = models.BooleanField()
    owner = models.IntegerField()
    ownerPassNum = models.IntegerField()
    arrivalTime = models.DateTimeField()
    dest = models.CharField(max_length=128)
    carType = models.CharField(max_length=20, blank = True, null = True, default=None)
    totalPassNum = models.IntegerField()
    
    specialRequest = models.CharField(blank = True, max_length=128, null = True, default=None)
    
    status = models.IntegerField(default=0)
    
    driver = models.IntegerField(blank = True, null=True, default=None)
    shared = models.JSONField(blank = True, null=True, default=None)
    
    def __str__(self) -> str:
        return "Ride ID: " + str(self.id) +" Ride Owner: " + str(self.owner)
    
    def addRidtoUser(rid, uid):
        user_obj = User.objects.get(pk=uid)
        rid_dict = user_obj.ride_list
        if rid_dict is None:
            rid_dict = {}
        if rid_dict[rid]:
            return False # already exist
        rid_dict[str(rid)] = True
        user_obj.ride_list = rid_dict
        user_obj.save()
        return True
    
    def rmRidfromUser(rid,uid):
        user_obj = User.objects.get(pk=uid)
        rid_dict = user_obj.ride_list
        if rid in rid_dict:
            del rid_dict[rid]
            user_obj.ride_list = rid_dict
            user_obj.save()
            return True
        else:
            return False # not exist
