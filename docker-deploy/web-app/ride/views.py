from django.http import HttpResponse
from django.shortcuts import *
from .models import Ride
from rideSharing.models import my_user as User
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
from .rideUtils import *
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# 未实现：异常抛出处理, check valid

@login_required
def index(request):
    if request.user.is_authenticated:
        return render(request,'ride/homepage.html')
    else:
        return redirect('rideSharing/login/')
    return render(request, 'ride/homepage.html', {})

@login_required
def getByRid(request, rid):
    ride = get_object_or_404(Ride, pk=rid)
    return HttpResponse(ride)

@login_required
def getByUid(request, uid):
    if request.method == 'GET':
        user_obj = User.objects.get(pk=uid)
        ride_list = list(user_obj.ride_list.keys())
        result = dict()
        count = 1
        for rid in ride_list:
            if user_obj.ride_list[rid] != "driver":
                result[count] = [Ride.objects.get(pk=rid),user_obj.ride_list[rid]]
                count += 1
        return HttpResponse(result)
    else:
        return HttpResponse("method wrong")

@login_required
def getByDid(request, uid):
    if request.method == 'GET':
        user_obj = User.objects.get(pk=uid)
        ride_list = list(user_obj.ride_list.keys())
        result = dict()
        count = 1
        for rid in ride_list:
            if user_obj.ride_list[rid] == "driver":
                result[count] = [Ride.objects.get(pk=rid),user_obj.ride_list[rid]]
                count += 1
        print(result)
        return HttpResponse(result)
    else:
        return HttpResponse("method wrong")

@login_required
def addRide(request):
    if request.method == "POST":
        data = request.POST.dict()
        dt = datetime.datetime.strptime(data['arrivalTime'], "%Y-%m-%d %H:%M:%S")
        data['arrivalTime'] = dt
        data['totalPassNum'] = data['ownerPassNum']
        ride_obj = Ride.objects.create(**data)
        if Ride.addRidtoUser(ride_obj.pk, data['owner'],"owner"):
            ride_obj.save()
            return HttpResponse(ride_obj.pk)
        else:
            return HttpResponse("User already exist")
    return HttpResponse("method wrong")

@login_required
def modifyRide(request):
    if request.method == 'PUT':
        data = MultiPartParser(request.META, request, request.upload_handlers).parse()[0].dict()
        ride = Ride.objects.get(pk = data['rid'])
        if int(data['status']) == 0 and ride.status == 0:
            if 'share_num' in data:
                share_dict = ride.shared
                if ride.shared is None:
                    share_dict = {}
                if data['uid'] in share_dict:
                    ride.totalPassNum -= share_dict[data['uid']]
                share_dict[data['uid']] = int(data['share_num'])
                ride.totalPassNum += int(data['share_num'])
                ride.shared = share_dict
                ride.save()
                Ride.addRidtoUser(ride.pk, data['uid'],"share")
                return HttpResponse("success add shared")
            elif int(data['uid']) == ride.owner:
                ride.totalPassNum -= ride.ownerPassNum
                ride.totalPassNum += int(data['ownerPassNum'])
                ride.rideType = data['rideType']
                ride.ownerPassNum = data['ownerPassNum']
                ride.dest = data['dest']
                ride.arrivalTime = datetime.datetime.strptime(data['arrivalTime'], "%Y-%m-%d %H:%M:%S")
                ride.specialRequest = data['specialRequest']
                ride.carType = data['carType']
                ride.save()
                return HttpResponse("owner modify success")
        elif int(data['status']) == 1 and ride.status == 0:
            ride.status=int(data['status'])
            ride.driver=int(data['uid'])
            if ride.driver == int(data['uid']):
                ride.save()
                Ride.addRidtoUser(ride.pk, ride.driver,"driver")
                return HttpResponse("Ride Confirmed")
        elif int(data['status']) == 2 and ride.status == 1:
            if ride.driver == int(data['uid']): 
                ride.status=int(data['status'])
                for uid in list(ride.shared.keys()):
                    Ride.rmRidfromUser(ride.pk, uid)
                Ride.rmRidfromUser(ride.pk,ride.owner)
                Ride.rmRidfromUser(ride.pk, ride.driver)
                sendEmail(ride)
                ride.save()
                return HttpResponse("send email")
        return HttpResponse("modify Unknown error")
    else:
        return HttpResponse("method wrong")

@login_required
def SearchRideDriver(request, uid):
    if request.method == 'GET':
        driver_obj = User.objects.get(pk=uid)
        driver_ride_list = list(driver_obj.ride_list.keys())
        result = Ride.objects.filter(totalPassNum__lte=driver_obj.max_passenger
                            ).filter(status=0
                            ).filter(Q(specialRequest = driver_obj.special_info)|Q(specialRequest = None)|Q(specialRequest = "")
                            ).filter(Q(carType = driver_obj.vehicle_type)|Q(carType = None)|Q(carType = "")
                            ).order_by('arrivalTime')
        for rid in driver_ride_list:
            result = result.exclude(pk=rid)
        return HttpResponse(result)
    else:
        return HttpResponse("method wrong")

@login_required
def SearchRideSharer(request):
    if request.method == 'GET':
        data = request.GET
        sharer_obj = User.objects.get(pk=data.get('uid'))
        sharer_ride_list = list(sharer_obj.ride_list.keys())
        max_time = datetime.datetime.strptime(data.get('max_time'), "%Y-%m-%d %H:%M:%S")
        min_time = datetime.datetime.strptime(data.get('min_time'), "%Y-%m-%d %H:%M:%S")
        result = Ride.objects.filter(dest = data.get('dest')
                            ).filter(arrivalTime__lte=max_time
                            ).filter(arrivalTime__gte=min_time
                            ).filter(rideType=True
                            ).order_by('arrivalTime')
        for rid in sharer_ride_list:
            result = result.exclude(pk=rid)
        return HttpResponse(result)
    else:
        return HttpResponse("method wrong")
