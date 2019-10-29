from django.urls import path
from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add', views.QuoteCreateView.as_view(), name='add_quote'),
]
