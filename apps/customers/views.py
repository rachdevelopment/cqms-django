from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView, CreateView
from django.utils import timezone

from .models import Customer
from .forms import CustomerForm

class IndexView(ListView):
    template_name = 'customers/index.html'
    
    def get_queryset(self):
        return []
    

class CustomerCreateView(FormView):
    template_name = 'customers/customer_form.html'    
    form_class = CustomerForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super().form_valid(form)    