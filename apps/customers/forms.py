from django import forms
from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput

from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'created_date', 'status']
        widgets = {
            'created_date': DatePickerInput(format='%d/%m/%Y'),    
        }

