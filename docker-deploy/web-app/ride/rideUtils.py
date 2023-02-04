from ride.models import Ride
from rideSharing.models import my_user as User
from django.core.mail import send_mail
def sendEmail(ride):
    user_list = [ride.owner]
    user_list += list(ride.shared.keys())
    for uid in user_list:
        user_obj = User.objects.get(pk=uid)
        msg = "Hi, "+ user_obj.username+"\n    your ride to the "+ride.dest+" at time "+str(ride.arrivalTime)+" is completed."
        send_mail(
            subject='Your order is complete',
            message=msg,
            from_email='13185812783@163.com',
            recipient_list=[user_obj.email],
            fail_silently=False
        )

def getByUid(request):
    user_obj = User.objects.get(pk=request.user.pk)
    if user_obj.ride_list == None or user_obj.ride_list == {}:
        return {}
    ride_list = list(user_obj.ride_list.keys())
    result = list()
    for rid in ride_list:
        if user_obj.ride_list[rid] != "driver":
            data = Ride.objects.get(pk=rid).to_dict()
            data['role'] = user_obj.ride_list[rid]
            result.append(data)
    print({"rideList":result})
    return {"rideList":result}

def getByDid(request):
    user_obj = User.objects.get(pk=request.user.pk)
    if user_obj.ride_list == None or user_obj.ride_list == {}:
        return None
    ride_list = list(user_obj.ride_list.keys())
    result = list()
    for rid in ride_list:
        if user_obj.ride_list[rid] == "driver":
            data = Ride.objects.get(pk=rid).to_dict()
            data['role'] = user_obj.ride_list[rid]
            result.append(data)
    print({"rideList":result})
    return {"rideList":result}

def checkValidUser(uid):
    return
