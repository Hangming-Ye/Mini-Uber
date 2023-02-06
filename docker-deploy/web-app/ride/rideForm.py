from django.forms import Form, ModelForm
from django import forms
from .models import Ride
from django.utils.translation import gettext_lazy as _

class AddRideForm(ModelForm):

    class Meta:
        model = Ride
        fields = ['rideType', 'ownerPassNum', 'arrivalTime', 'dest','carType','specialRequest']

        help_texts = {
            'carType': _('Optional'),
            'SpecialRequest': _('Optional'),
            'arrivalTime': _('Format: YYYY-MM-DD HH:MM'),
        }
  
    # def __init__(self,*args,**kwargs):
    #     super(ModelForm,self).__init__(*args,**kwargs)
  
    #     for fieldname in self.base_fields:
    #         field = self.base_fields[fieldname]

class ModifyShareForm(Form):
    Sharer_Passenger_Number = forms.IntegerField(min_value=1)

class SearchShareForm(Form):
    Destination = forms.CharField(required=True)
    Maximum_Arrival_Time = forms.DateTimeField(required=True)
    Minimum_Arrival_Time = forms.DateTimeField(required=True)
    







