import datetime

from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices
from softdelete.models import SoftDeleteObject

class Quote(SoftDeleteObject, TimeStampedModel, StatusModel, models.Model):
    all_objects = models.Manager()
    
    customer_name = models.CharField(max_length = 255)
    customer_order_number = models.CharField(max_length = 30)
    subtotal = MoneyField(max_digits=19, decimal_places=2, default_currency='AUD', default=0)
    #status = models.CharField(max_length = 30)
    #created_date = models.DateTimeField()
    delivery_due_date = models.DateTimeField()
    ordered_date = models.DateTimeField()
    STATUS = Choices('Entry', 'Quote', 'Ordered', 'In Process','Cancelled','Enroute', 'Delivered', 'Invoiced', 'Completed')
    
    def __str__(self):
        return self.customer_order_number
    
    def was_created_today(self):        
        return datetime.date.today() == self.created.date()
    
    def was_ordered_today(self):
        return datetime.date.today() == self.ordered_date.date()
    
    def is_due_today(self):
        return datetime.date.today() == self.delivery_due_date.date()
        
    was_created_today.boolean = True
    was_created_today.short_description = 'Created today?'
    
    was_ordered_today.boolean = True
    was_ordered_today.short_description = 'Ordered today?'
    
    is_due_today.boolean = True
    is_due_today.short_description = 'Due today?'
    