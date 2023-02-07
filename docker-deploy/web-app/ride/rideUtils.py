from ride.models import Ride
from rideSharing.models import my_user as User
from django.core.mail import send_mail
def sendEmail(ride):
    user_list = [ride.owner]
    if ride.shared:
        user_list += list(ride.shared.keys())
    else:
        ride.shared = {}
        ride.save()
    for uid in user_list:
        user_obj = User.objects.get(pk=uid)
        msg = "Hi, "+ user_obj.username+"\n    your ride to the "+ride.dest+" at time "+str(ride.arrivalTime)+" is confirmed. No further changes are allowed. Please login to see the detailed information."
        send_mail(
            subject='Your order is confirmed',
            message=msg,
            from_email='Duke_ECE568_RSS@outlook.com',
            recipient_list=[user_obj.email],
            fail_silently=False
        )
        
def getByUid(request):
    user_obj = User.objects.get(pk=request.user.pk)
    if user_obj.ride_list == None or user_obj.ride_list == {}:
        user_obj.ride_list = {}
        return {}
    ride_list = list(user_obj.ride_list.keys())
    result = list()
    for rid in ride_list:
        data = Ride.objects.get(pk=rid).to_dict()
        data['role'] = user_obj.ride_list[rid]
        result.append(data)
    return {"rideList":result}
    
