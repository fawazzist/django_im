from django import forms
from .models import Delivery

class startDeliveryFrom(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['quantity','serial_number','delivery_date']


class assignDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['is_delivered','is_accepted']




        