from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'dashboard/index.html'
    context_object_name = 'latest_orders_list'
    
    def get_queryset(self):
        """ 
        Return the 10 most recently created quotes
        """
        return Quote.objects.filter(ordered_date__lte=timezone.now()).order_by('-ordered_date')[:10]