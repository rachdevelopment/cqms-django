import datetime

from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

class Customer(models.Model):
    customer_name = models.CharField(max_length = 255)
    abn = models.CharField(max_length = 11)    
    status = models.CharField(max_length = 30)
    credit_limit = MoneyField(max_digits=19, decimal_places=2, default_currency='AUD', default=0)
    created_date = models.DateTimeField()
    
    def __str__(self):
        return self.customer_name
    
    def was_created_today(self):        
        return datetime.date.today() == self.created_date.date()
    
    was_created_today.boolean = True
    was_created_today.short_description = 'Created today?'
