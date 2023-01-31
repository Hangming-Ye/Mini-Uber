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

<<<<<<< Updated upstream
    def __str__(self):
        return self.user_name
=======
# a driver is a user (inheritance)
class Driver(User):
    #???????length
    vehicle_type = models.CharField(max_length=10)
    license_plate_num = models.CharField(max_length=8)
    special_info = models.TextField()
    max_passenger = models.IntegerField()


>>>>>>> Stashed changes
