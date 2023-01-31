from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from .models import User
# Create your views here.

# user register:
def user_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get("email")
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # username already exists:
        if User.objects.filter(username=username):
            # ?????? user_reg.html ??????
            return render(request, 'rideSharing/user_reg.html', {'error_reg': "Username already exists"})
        else:
            if password1 == password2:
                # The passwords entered twice match:
                user = User.objects.create_user(username=username, email=email, password=password1, is_driver=False)
                user.save()
                return redirect('login')
            else:
                # The passwords entered twice do not match:
                return render(request, 'rideSharing/user_reg.html', {'error_reg': "The passwords entered twice do not match!"})
    return render(request, 'rideSharing/user_reg.html')

# user login:
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            user = auth.authenticate(username=username, password=password)
            # user.is_active???????????
            # if user is not None:???????
            if user:
                auth.login(request, user)
                return redirect('homepage', {'user', user})
            else:
                return render(request, 'rideSharing/login.html', {'login_password_error' : 'password is incorrect'})
        else:
            return render(request, 'rideSharing/login.html', {'login_username_error' : 'this user does not exist'})
    else:
        render(request, 'rideSharing/login.html')


# user logout:
def logout(request):
    auth.logout(request)
    return redirect('login')

# homepage:
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'rideSharing/home.html')
    else:
        return redirect('login')


def driver_register(request):
    