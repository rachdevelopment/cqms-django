import datetime

from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices
from softdelete.models import SoftDeleteObject

class Customer(SoftDeleteObject, TimeStampedModel, StatusModel, models.Model):
    all_objects = models.Manager()
    
    '''Field definitions'''
    customer_name = models.CharField(max_length = 255)    
    abn = models.CharField(max_length = 11)        
    credit_limit = MoneyField(max_digits=19, decimal_places=2, default_currency='AUD', default=0)
    STATUS = Choices('Active', 'Inactive', 'On Hold', 'On Stop')
    
    '''Method definitions'''
    def __str__(self):
        return self.customer_name
    
    def was_created_today(self):        
        return datetime.date.today() == self.created.date()
        
    was_created_today.boolean = True
    was_created_today.short_description = 'Created today?'