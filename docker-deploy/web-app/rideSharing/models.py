from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class my_user(User):
    #????? user id?????
    #????? driver ?????
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

    #user_name = models.CharField(max_length=16,unique=True)
    #email = models.EmailField()
    #password = models.CharField(max_length=256)

    is_driver = models.BooleanField(default=False)

    vehicle_type = models.CharField(choices=CAR_TYPE_CHOICES, max_length=20, blank = True, null=True, default=None)
    license_plate_nums = models.CharField(blank = True, max_length=8, null=True, default=None)
    special_info = models.TextField(blank = True, null=True, default=None)
    max_passenger = models.IntegerField(blank = True, null=True, default=None)

    ride_list = models.JSONField(blank = True, null=True, default=None)
    def __str__(self):
        return self.username