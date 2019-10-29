import datetime
import sys

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone


from .models import Quote
from test.test_htmlparser import TestCaseBase

class QuoteModelTests(TestCase):
    
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
        future_quote = Quote(delivery_due_date=time,ordered_date=time)
        
        self.assertIs(future_quote.is_due_today(), False)

    def test_is_due_today_with_past_date(self):
        """
        is_due_today() returns False for questions whose delivery_due_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_quote = Quote(delivery_due_date=time,ordered_date=time)
        
        self.assertIs(past_quote.is_due_today(), False)
    
    def test_is_due_today_with_current_date(self):
        """
        is_due_today() returns True for questions whose delivery_due_date
        is today.
        """
        today = timezone.now()
        today_quote = Quote(delivery_due_date=today,ordered_date=today)
        self.assertIs(today_quote.is_due_today(), True)   
        
    def test_soft_delete(self):        
        today = timezone.now()
        quote = create_quote(today, 'test customer') #Quote(delivery_due_date=today,ordered_date=today)
        id = quote.pk
        sys.stderr.write('quote with ' + repr(quote.id) + ': customer_name = ' + quote.customer_name + ' deleted at = ' + repr(quote.deleted_at) + '\n')
        self.assertIs(quote.is_due_today(), True)
        
        quote.delete();
        self.assertIsNotNone(quote.deleted_at)
        
        deleted_quote = Quote.all_objects.get(id = quote.id)
        sys.stderr.write('deleted quote with ' + repr(deleted_quote.id) + ': customer_name = ' + deleted_quote.customer_name + ' deleted at = ' + repr(deleted_quote.deleted_at) + '\n')
                
        self.assertEqual(id, deleted_quote.pk, "id's are not equal")
        
        deleted_quote.undelete()
        
        #self.assertIsNone(deleted_quote.deleted_at)
        
        restored_quote = Quote.objects.get(id = quote.id)
        sys.stderr.write('restored quote with ' + repr(restored_quote.id) + ': customer_name = ' + restored_quote.customer_name + ' deleted at = ' + repr(restored_quote.deleted_at) + '\n')
        self.assertIsNone(restored_quote.deleted_at)
        

def create_quote(date, customer_name):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Quote.objects.create(customer_name=customer_name,delivery_due_date=date,ordered_date=date)        
          