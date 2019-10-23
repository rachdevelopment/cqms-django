from django.views import generic
from django.utils import timezone

from .models import Quote

class IndexView(generic.ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'latest_quotes_list'
    
    def get_queryset(self):
        """ 
        Return the 10 most recently created quotes
        """
        return Quote.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:10]