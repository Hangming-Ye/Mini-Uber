from django.http import HttpResponse
from django.shortcuts import *
from .models import Ride
from rideSharing.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
import sys
import utils
# 未实现：异常抛出处理, check valid

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the ride index.")

def getByRid(request, rid):
    ride = get_object_or_404(Ride, pk=rid)
    return HttpResponse(ride)

def getByUid(request, uid):
    if request.method == 'GET':
        data = request.GET.dict()
        user_obj = User.objects.get(pk=data['uid'])
        ride_list = user_obj.ride_list.keys()
        result = dict()
        count = 1
        for rid in ride_list:
            result[count] = [Ride.objects.get(pk=rid),ride_list[rid]]
        return result
    else:
        return HttpResponse("method wrong")

@csrf_exempt
def addRide(request):
    if request.method == "POST":
        data = request.POST.dict()
        dt = datetime.datetime.strptime(data['arrivalTime'], "%Y-%m-%d %H:%M:%S")
        data['arrivalTime'] = dt
        if 'driver' in data or 'share' in data:
            return HttpResponse("data error")
        data['totalPassNum'] = data['ownerPassNum']
        ride_obj = Ride.objects.create(**data)

        ride_obj.save()
        Ride.addRidtoUser(ride_obj.rid, data.uid,"owner")
        return HttpResponse(ride_obj)
    return HttpResponse("method wrong")

@csrf_exempt
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
                share_dict[data['uid']] = data['share_num']
                ride.totalPassNum += data['share_num']
                ride.shared = share_dict
                ride.save()
                Ride.addRidtoUser(ride.rid, data.uid,"share")
                return HttpResponse("success add shared")
            elif int(data['uid']) == ride.owner:
                ride.totalPassNum -= ride.ownerPassNum
                ride.totalPassNum += data['ownerPassNum']
                ride.rideType = data['rideType']
                ride.ownerPassNum = data['ownerPassNum']
                ride.dest = data['dest']
                ride.arrivalTime = datetime.datetime.strptime(data['arrivalTime'], "%Y-%m-%d %H:%M:%S")
                ride.specialRequest = data['specialRequest']
                ride.carType = data['carType']
                ride.save()
                return HttpResponse("modify success")
        elif int(data['status']) == 1 and ride.status == 0:
            ride.status=int(data['status'])
            ride.driver=int(data['uid'])
            ride.save()
            Ride.addRidtoUser(ride.pk, ride.driver,"driver")
            return HttpResponse("add driver")
        elif int(data['status']) == 2 and ride.status == 1:
            if ride.driver == uid: 
                ride.status=int(data['status'])
                for uid in ride.shared.keys():
                    Ride.rmRidfromUser(ride.pk, uid)
                Ride.rmRidfromUser(ride.pk,ride.owner)
                Ride.rmRidfromUser(ride.pk, ride.driver)
                ride.save()
                utils.sendEmail(ride)
                return HttpResponse("send email")
        HttpResponse("data error")
    return HttpResponse("method wrong")

def SearchRideDriver(request):
    if request.method == 'GET':
        data = request.GET.dict()
        driver_obj = User.objects.get(pk=data['uid'])
        driver_ride_list = driver_obj.ride_list.keys()
        result = Ride.objects.filter(totalPassNum__lte=driver_obj.max_passenger
                            ).filter(status=0
                            ).filter(specialRequest = driver_obj.special_info
                            ).order_by('arrivalTime')
        result = Ride.objects.filter(carType = driver_obj.vehicle_type)
        for rid in driver_ride_list:
            result = result.exclude(pk=rid)
        return result
    else:
        return HttpResponse("method wrong")

def SearchRideSharer(request):
    if request.method == 'GET':
        data = request.GET.dict()
        sharer_obj = User.objects.get(pk=data['uid'])
        sharer_ride_list = sharer_obj.ride_list.keys()
        result = Ride.objects.filter(dest = data['dest']
                            ).filter(arrivalTime__lte=data['max_time']
                            ).filter(arrivalTime__gte=data['min_time']
                            ).order_by('arrivalTime')
        for rid in sharer_ride_list:
            result = result.exclude(pk=rid)
        return result
    else:
        return HttpResponse("method wrong")
