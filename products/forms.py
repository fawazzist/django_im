from django import forms
from .models import Producer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['brand_name', 'stock']
