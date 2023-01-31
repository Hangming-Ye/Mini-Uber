from django.db import models

# Create your models here.

class User(models.Model):
    #????? user id?????
    #????? driver ?????
    user_name = models.CharField(max_length=16,unique=True)
    email = models.EmailField()
    #salt??????
    password = models.CharField(max_length=256)
    is_driver = models.BooleanField()

    vehicle_type = models.CharField(max_length=10, null=True)
    license_plate_num = models.CharField(max_length=8,null=True)
    special_info = models.TextField(null=True)
    max_passenger = models.IntegerField(null=True)

    def __str__(self):
        return self.user_name