from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView, CreateView
from django.utils import timezone

from .models import Quote
from .forms import QuoteForm

class IndexView(ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'latest_quotes_list'
    
    def get_queryset(self):
        """ 
        Return the 10 most recently created quotes
        """
        return Quote.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:10]
    
    
class QuoteCreateView(FormView):
    template_name = 'quotes/quote_form.html'    
    form_class = QuoteForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super().form_valid(form)