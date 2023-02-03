from ride.models import Ride
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import auth
from .models import my_user as User
# Create your views here.

# user register:
def user_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # username already exists:
        if User.objects.filter(username=username):
            # ?????? user_reg.html ??????
            return render(request, 'rideSharing/user_reg.html', {'error_reg': 'Username already exists!!!'})
        else:
            if password == confirm_password:
                # The passwords entered twice match:
                # vehicle_type=None, license_plate_nums=None, special_info=None, max_passenger=None
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/rideSharing/login/')
            else:
                # The passwords entered twice do not match:
                return render(request, 'rideSharing/user_reg.html', {'error_reg': 'The passwords entered twice do not match!!!'})
    return render(request, 'rideSharing/user_reg.html')

# user login:
def login(request):
    # return render(request, 'rideSharing/login.html', {"num": "views_num"})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            user = auth.authenticate(username=username, password=password)
            # user.is_active???????????
            if user is not None:
                auth.login(request, user)
                return redirect('/rideSharing/homepage/', {'user', user})
            else:
                return render(request, 'rideSharing/login.html', {'login_password_error' : 'Password is incorrect!!!'})
        else:
            return render(request, 'rideSharing/login.html', {'login_username_error' : 'This user does not exist!!!'})
    return render(request, 'rideSharing/login.html')


# user logout:
def logout(request):
    # Check whether the user is logged in
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/rideSharing/login/')

# homepage:
def homepage(request):
    # Check whether the user is logged in
    if request.user.is_authenticated:
        return render(request, 'rideSharing/home.html')
    else:
        return redirect('/rideSharing/login/')


# User should be able to view their driver status as well as personal & vehicle info:
def get_user_info(request):
    # Check whether the user is logged in
    if request.user.is_authenticated == False:
        return redirect('/rideSharing/login/')
    else:
        # user = User.objects.filter(pk=request.user.pk).values()
        user = User.objects.get(pk = request.user.pk)
        context = {
            'username': user.username,
            'email': user.email,
            'is_driver': user.is_driver,
            'vehicle_type': user.vehicle_type,
            'license_plate_nums': user.license_plate_nums,
            'special_info': user.special_info,
            'max_passenger': user.max_passenger,
        }
        # html??????????
        return render(request, 'rideSharing/get_user_info.html', context)

# A registered driver cancels the register and become a pure user (de-reg):
def driver_de_register(request):
    user = User.objects.get(pk = request.user.pk)
    uid = request.user.pk
    # traverse all rides of this user, and get the incomplete rides in which the role of this user is driver
    # ??????????????? incomplete???????
    # ?????????????value是这种形式嘛？这样写可以嘛？？？？？？
    # rid_list = list(filter(lambda x: user.ride_list[x] == 'driver', user.ride_list))
    rid_list = []
    for rid0 in user.ride_list.keys():
        if user.ride_list[rid0] == 'driver':
            rid_list.append(rid0)
    # Change all these rides status into open and driver field in ride object into None
    # remove these rides from this user's ride dictionary
    for rid1 in rid_list:
        ride = Ride.objects.get(pk = rid1)
        ride.status = 0
        ride.driver = None
        ride.save()
        Ride.rmRidfromUser(rid1,uid)
    # Change all driver info into None in this user object and is_driver into False
    user.vehicle_type = None
    user.special_info = None
    user.license_plate_nums = None
    user.max_passenger = None
    user.is_driver = False
    return redirect('/rideSharing/get_user_info/')

# User should be able to edit their driver status as well as personal & vehicle info:
# It is used for Driver Registration and edit driver info
def modify_driver(request):
    # Check whether the user is logged in
    if request.user.is_authenticated == False:
        return redirect('/rideSharing/login/')
    user = User.objects.get(pk = request.user.pk)
    if request.method == 'POST':
        username = request.POST.get('username')
        user.username = username
        vehicle_type = request.POST.get('vehicle_type')
        license_plate_nums = request.POST.get('license_plate_nums')
        special_info = request.POST.get('special_info')
        max_passenger = request.POST.get('max_passenger')
        user.vehicle_type = vehicle_type
        user.special_info = special_info
        user.license_plate_nums = license_plate_nums
        user.max_passenger = max_passenger
        # Whether it is editing driver information or registering as a driver, is_driver is always True
        user.is_driver = True
        user.save()        
        return redirect('/rideSharing/get_user_info/')
    return render(request, 'rideSharing/modify_driver.html')

