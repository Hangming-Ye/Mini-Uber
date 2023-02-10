from django.db import models
from rideSharing.models import my_user as User

class Ride(models.Model):
    CAR_TYPE_CHOICES =(
    ("SUV", "SUV"),
    ("Hatchback", "Hatchback"),
    ("Crossover", "Crossover"),
    ("Convertible", "Convertible"),
    ("Sedan", "Sedan"),
    ("Sports Car", "Sports Car"),
    ("Coupe", "Coupe"),
    ("Minivan", "Minivan"),
    ("Station Wagon", "Station Wagon"),
    ("Pickup Truck", "Pickup Truck"),
    )

    rideType = models.BooleanField()
    owner = models.IntegerField()
    ownerPassNum = models.IntegerField()
    arrivalTime = models.DateTimeField()
    dest = models.CharField(max_length=128)
    carType = models.CharField(choices=CAR_TYPE_CHOICES, max_length=20, blank = True, null=True, default=None)
    totalPassNum = models.IntegerField()
    
    specialRequest = models.CharField(blank = True, max_length=128, null = True, default=None)
    
    status = models.CharField(default="Open",max_length=10)
    
    driver = models.IntegerField(blank = True, null=True, default=None)
    shared = models.JSONField(blank = True, null=True, default=dict)
    
    def __str__(self) -> str:
        return "Ride ID: " + str(self.id) +" Ride Owner: " + str(self.owner)

    def to_dict(self):
        data = {}
        data["rid"] = self.pk
        data["rideType"] = "Share Ride" if self.rideType else "Non-share Ride"
        ownername = User.objects.get(pk=self.owner).username
        data["owner"] = ownername

        data["ownerPassNum"] = self.ownerPassNum
        data["arrivalTime"] = self.arrivalTime
        data["dest"] = self.dest
        data["carType"] = self.carType
        data["totalPassNum"] = self.totalPassNum
        data["specialRequest"] =  "None" if self.specialRequest is None else self.specialRequest
        data["status"] = self.status

        if self.rideType:
            data["shared"] = {"share_num":0,"share_pass_num":0} if self.shared is None else {
                "share_num":len(list(self.shared)),"share_pass_num":self.totalPassNum - self.ownerPassNum}

        if self.driver != None:
            data["driver"] = self.driver
            
            driver_obj = User.objects.get(pk=self.driver)
            
            data["driverName"] = driver_obj.realName
            data["carNum"] = driver_obj.license_plate_nums
            data["maxCapacity"] = driver_obj.max_passenger
            data["dcarType"] = driver_obj.vehicle_type
            data["dSpecialInfo"] = "None" if driver_obj.special_info is None else driver_obj.special_info
        return data


    def addRidtoUser(rid, uid, role):
        user_obj = User.objects.get(id=uid)
        rid_dict = user_obj.ride_list
        if rid_dict is None:
            rid_dict = {}
        if rid in rid_dict:
            return False
        rid_dict[rid] = role
        user_obj.ride_list = rid_dict
        user_obj.save()
        return True
    
    def rmRidfromUser(rid,uid):
        user_obj = User.objects.get(pk=uid)
        rid_dict = user_obj.ride_list
        if rid_dict is None:
            rid_dict = {}
        if str(rid) in rid_dict:
            del rid_dict[str(rid)]
            user_obj.ride_list = rid_dict
            user_obj.save()
            return True
        else:
            return False