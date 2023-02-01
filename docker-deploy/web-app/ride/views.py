from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import *
from .models import Ride
from rideSharing.models import User
import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser

#未实现：根据身份返回，根据当前人数判断是否能添加，加入增加list,结束删除list,异常抛出处理,加入share时的重复与验证问题

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the ride index.")

def getByRid(request, rid):
    ride = get_object_or_404(Ride, pk=rid)
    return HttpResponse(ride)

def getByUid(request, uid):
    user = get_object_or_404(User, pk = uid)

@csrf_exempt 
def addRide(request):
    if request.method == "POST":
        data = request.POST.dict()
        dt = datetime.datetime.strptime(data['arrivalTime'], "%Y-%m-%d %H:%M:%S")
        data['arrivalTime'] = dt
        if 'driver' in data or 'share' in data:
            return HttpResponse("data error")
        ride_obj = Ride.objects.create(**data)
        ride_obj.save()
        return HttpResponse(ride_obj)
    return HttpResponse("method wrong")

@csrf_exempt
def modifyRide(request):
    if request.method == 'PUT':
        data = MultiPartParser(request.META, request, request.upload_handlers).parse()[0].dict()
        print(data)
        ride = get_object_or_404(Ride, pk = data['rid'])
        if int(data['status']) == 0 and ride.status == 0:
            if 'share_id' in data and 'share_num' in data:
                if ride.shared is None:
                    share_dict = {}
                else:
                    share_dict = ride.shared
                share_dict[data['share_id']] = data['share_num']
                ride.shared = share_dict
                ride.save()
                return HttpResponse("success add")
            elif int(data['uid']) == ride.owner:
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
            return HttpResponse("add driver")
        elif int(data['status']) == 2 and ride.status == 1:
            ride.status=int(data['status'])
            # delete in the user rid list
            return HttpResponse("send email")
            ride.save()
        HttpResponse("data error")
    return HttpResponse("method wrong")
