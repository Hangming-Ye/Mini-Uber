from django.forms import Form, ModelForm
from django import forms
from .models import Ride
from django.utils.translation import gettext_lazy as _

class AddRideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['rideType', 'ownerPassNum', 'arrivalTime', 'dest','carType','specialRequest']

        labels = {
            'rideType': _('Is Sharable'),
            'ownerPassNum': _('Passenger Number of Owner'),
            'dest': _('Destination'),
            'carType': _('Car Type'),
            'arrivalTime': _('Arrival Time'),
            'specialRequest': _('Special Request'),
        }
        help_texts = {
            'carType': 'Optional',
            'specialRequest': 'Optional',
            'arrivalTime': 'Format: YYYY-MM-DD HH:MM',
        }

class ModifyShareRideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['ownerPassNum', 'carType','specialRequest']

        labels = {
            'ownerPassNum': _('Passenger Number of Owner'),
            'carType': _('Car Type'),
            'specialRequest': _('Special Request'),
        }
        help_texts = {
            'carType': 'Optional',
            'specialRequest': 'Optional',
        }

class ModifyShareForm(Form):
    Sharer_Passenger_Number = forms.IntegerField(min_value=1)

class SearchShareForm(Form):
    Destination = forms.CharField(required=True)
    Maximum_Arrival_Time = forms.DateTimeField(required=True, help_text='Format: YYYY-MM-DD HH:MM')
    Minimum_Arrival_Time = forms.DateTimeField(required=True, help_text='Format: YYYY-MM-DD HH:MM')
    







