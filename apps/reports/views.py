from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'reports/index.html'
    
    def get_queryset(self):
        return []