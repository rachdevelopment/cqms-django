from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'scheduling/index.html'
    
    def get_queryset(self):
        return []