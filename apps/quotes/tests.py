import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone


from .models import Quote
from test.test_htmlparser import TestCaseBase

class QuoteModelTests(TestCase):
    
    def test_was_created_today_with_future_date(self):
        """ 
        was_created_today() returns False for questions 
        whose created_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_quote = Quote(created_date=time)
        
        self.assertIs(future_quote.was_created_today(), False)

    def test_was_created_today_with_past_date(self):
        """
        was_created_today() returns False for questions whose created_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_quote = Quote(created_date=time)
        
        self.assertIs(past_quote.was_created_today(), False)
    
    def test_was_created_today_with_current_date(self):
        """
        was_created_today() returns True for questions whose created_date
        is today.
        """
        today = timezone.now()
        today_quote = Quote(created_date=today)
        self.assertIs(today_quote.was_created_today(), True)   
        
        
        
    def test_was_ordered_today_with_future_date(self):
        """ 
        was_ordered_today() returns False for questions 
        whose ordered_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_quote = Quote(ordered_date=time)
        
        self.assertIs(future_quote.was_ordered_today(), False)

    def test_was_ordered_today_with_past_date(self):
        """
        was_ordered_today() returns False for questions whose ordered_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_quote = Quote(ordered_date=time)
        
        self.assertIs(past_quote.was_ordered_today(), False)
    
    def test_was_ordered_today_with_current_date(self):
        """
        was_ordered_today() returns True for questions whose ordered_date
        is today.
        """
        today = timezone.now()
        today_quote = Quote(ordered_date=today)
        self.assertIs(today_quote.was_ordered_today(), True)   
        
        
        
    def test_is_due_today_with_future_date(self):
        """ 
        is_due_today() returns False for questions 
        whose delivery_due_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_quote = Quote(delivery_due_date=time)
        
        self.assertIs(future_quote.is_due_today(), False)

    def test_is_due_today_with_past_date(self):
        """
        is_due_today() returns False for questions whose delivery_due_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_quote = Quote(delivery_due_date=time)
        
        self.assertIs(past_quote.is_due_today(), False)
    
    def test_is_due_today_with_current_date(self):
        """
        is_due_today() returns True for questions whose delivery_due_date
        is today.
        """
        today = timezone.now()
        today_quote = Quote(delivery_due_date=today)
        self.assertIs(today_quote.is_due_today(), True)   
        
        