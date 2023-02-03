from ride.models import Ride
from rideSharing.models import my_user as User
from django.core.mail import send_mail
def sendEmail(ride):
    user_list = [ride.owner]
    user_list += list(ride.shared.keys())
    for uid in user_list:
        user_obj = User.objects.get(pk=uid)
        msg = "Hi, "+ user_obj.username+"\n    your ride to the "+ride.dest+" at time "+str(ride.arrivalTime)+" is completed."
        print(msg)
        send_mail(
            subject='Your order is complete',
            message=msg,
            from_email='13185812783@163.com',
            recipient_list=[user_obj.email],
            fail_silently=False
        )

def checkValidUser(uid):
    return
