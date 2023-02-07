from django.http import HttpResponse
from django.shortcuts import *
from .models import Ride
from rideSharing.models import my_user as User
from .rideUtils import *
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .rideForm import *

@login_required
def index(request):
    if request.user.is_authenticated:
        data = getByUid(request)
        user = User.objects.get(pk=request.user.pk)
        data["user"] = user
        return render(request,'ride/homepage.html',data)
    else:
        return redirect('rideSharing/login/')

@login_required
def getByRid(request, rid, role):
    ride = get_object_or_404(Ride, pk=rid)
    ride_dict = ride.to_dict()
    ride_dict["role"] = role
    data = {"ride":ride_dict}
    user = User.objects.get(pk=request.user.pk)
    data["user"] = user

    return render(request,'ride/detail.html',data)

@login_required
def addRide(request):
    uid = request.user.id
    if request.method == 'POST':
        form = AddRideForm(request.POST)
        if form.is_valid():
            ride_obj = form.save(commit=False)
            ride_obj.owner = uid
            ride_obj.totalPassNum = ride_obj.ownerPassNum
            ride_obj.save()
            Ride.addRidtoUser(ride_obj.pk, uid,"owner")
            return redirect('/ride/homepage/')
        else:
            return render(request, 'ride/newRequest.html', {'form': form,'error':"Data Error: please check the input format."})
    else:
        form = AddRideForm()
        return render(request, 'ride/newRequest.html', {'form': form})

@login_required
def modifyRide(request, rid):
    ride_obj = Ride.objects.get(pk=rid)
    if ride_obj.shared == None or ride_obj.shared == dict():
        if request.method == 'POST':
            form = AddRideForm(request.POST, instance=ride_obj)
            if form.is_valid():
                ride_obj = Ride.objects.get(pk=rid)
                total = ride_obj.totalPassNum + form.cleaned_data['ownerPassNum'] - ride_obj.ownerPassNum
                ride_obj.totalPassNum = total
                ride_obj.ownerPassNum = form.cleaned_data['ownerPassNum']
                ride_obj.carType = form.cleaned_data['carType']
                ride_obj.specialRequest = form.cleaned_data['specialRequest']
                ride_obj.arrivalTime = form.cleaned_data['arrivalTime']
                ride_obj.dest = form.cleaned_data['dest']
                ride_obj.save()
                return redirect('/ride/homepage/')
            else:
                return render(request, 'ride/newRequest.html', {'form': form,'error':"Data Error: please check the input format."})
        else:
            form = AddRideForm(instance=ride_obj)
            return render(request, 'ride/newRequest.html', {'form': form})
    else:
        if request.method == 'POST':
            form = ModifyShareRideForm(request.POST, instance=ride_obj)
            if form.is_valid():
                ride_obj = Ride.objects.get(pk=rid)
                total = ride_obj.totalPassNum + form.cleaned_data['ownerPassNum'] - ride_obj.ownerPassNum
                ride_obj.totalPassNum = total
                ride_obj.ownerPassNum = form.cleaned_data['ownerPassNum']
                ride_obj.carType = form.cleaned_data['carType']
                ride_obj.specialRequest = form.cleaned_data['specialRequest']
                ride_obj.save()
                return redirect('/ride/homepage/')
            else:
                return render(request, 'ride/modifyRequest.html', {'form': form})
        else:
            form = ModifyShareRideForm(instance=ride_obj)
            return render(request, 'ride/modifyRequest.html', {'form': form})

@login_required
def addShare(request, rid):
    uid = request.user.id
    ride_obj = Ride.objects.get(pk=rid)
    if request.method == 'POST':
        form = ModifyShareForm(request.POST)
        if form.is_valid():
            share_dict = ride_obj.shared
            if share_dict is None:
                share_dict = {}
            if str(uid) in share_dict:
                ride_obj.totalPassNum -= share_dict[str(uid)]
            else:
                Ride.addRidtoUser(rid, uid,"sharer")
            share_dict[str(uid)] = form.cleaned_data['Sharer_Passenger_Number']
            ride_obj.totalPassNum += form.cleaned_data['Sharer_Passenger_Number']
            ride_obj.shared = share_dict
            ride_obj.save()
        return redirect('/ride/homepage/')
    else:
        form = ModifyShareForm()
        return render(request, 'ride/shareRide.html', {'form': form})

@login_required
def confirmRide(request, rid):
    ride = Ride.objects.get(pk = rid)
    ride.status="Confirmed"
    ride.driver= request.user.id
    ride.save()
    sendEmail(ride)
    Ride.addRidtoUser(ride.pk, ride.driver,"driver")
    return redirect('/ride/homepage/')

@login_required
def completeRide(request, rid):
    ride = Ride.objects.get(pk = rid)
    if ride.driver == request.user.id: 
        ride.status="Complete"
    if ride.shared is None:
        ride.shared = {}
    for uid in list(ride.shared.keys()):
        Ride.rmRidfromUser(ride.pk, uid)
    Ride.rmRidfromUser(ride.pk,ride.owner)
    Ride.rmRidfromUser(ride.pk, ride.driver)
    ride.save()
    return redirect('/ride/homepage/')

@login_required
def SearchRideDriver(request):
    if request.method == 'GET':
        driver_obj = User.objects.get(pk=request.user.pk)
        if driver_obj.ride_list == None:
            driver_obj.ride_list  = dict()
        driver_ride_list = list(driver_obj.ride_list.keys())
        result = Ride.objects.filter(totalPassNum__lte=driver_obj.max_passenger
                            ).filter(status="Open"
                            ).filter(Q(specialRequest = driver_obj.special_info)|Q(specialRequest = None)|Q(specialRequest = "")
                            ).filter(Q(carType = driver_obj.vehicle_type)|Q(carType = None)|Q(carType = "")
                            ).order_by('+arrivalTime')
        for rid in driver_ride_list:
            result = result.exclude(pk=rid)
        result_list = list()
        for ride in result:
            ride = ride.to_dict()
            result_list.append(ride)
        return render(request,'ride/driver_page.html',{'rideList':result_list})
    else:
        return HttpResponse("method wrong")

@login_required
def SearchRideSharer(request):
    if request.method == 'POST':
        uid = request.user.id
        form = SearchShareForm(request.POST)
        sharer_obj = User.objects.get(pk=uid)
        if form.is_valid():
            if sharer_obj.ride_list == None:
                sharer_obj.ride_list  = dict()
            sharer_ride_list = list(sharer_obj.ride_list.keys())
            max_time = form.cleaned_data['Maximum_Arrival_Time']
            min_time = form.cleaned_data['Minimum_Arrival_Time']
            dest = form.cleaned_data['Destination']
            result = Ride.objects.filter(dest = dest
                                ).filter(arrivalTime__lte=max_time
                                ).filter(arrivalTime__gte=min_time
                                ).filter(rideType=True
                                ).filter(status="Open"
                                ).order_by('arrivalTime')
            for rid in sharer_ride_list:
                result = result.exclude(pk=rid)
            result_list = list()
            for ride in result:
                ride = ride.to_dict()
                result_list.append(ride)
            return render(request,'ride/shareSearchPage.html',{'rideList':result_list})
        else:
            return render(request, 'ride/shareForm.html', {'form': form,'error':"Data Error: please check the input format."})
    else:
        form = SearchShareForm()
        return render(request, 'ride/shareForm.html', {'form': form})
