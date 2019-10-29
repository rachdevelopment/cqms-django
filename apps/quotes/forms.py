from django import forms
from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput

from .models import Quote

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['customer_name', 'customer_order_number', 'subtotal', 'status', 'delivery_due_date', 'ordered_date']
        widgets = {        
            'delivery_due_date': DatePickerInput(format='%d/%m/%Y'),    
            'ordered_date': DatePickerInput(format='%d/%m/%Y'),    
        }

