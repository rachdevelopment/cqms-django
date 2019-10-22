"""cqms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView

from apps.dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url( 'login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url( 'logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    #url( r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^$', login_required(dashboard_views.IndexView.as_view()), name='home'),
    path('dashboard/', include('apps.dashboard.urls')),
    path('scheduling/', include('apps.scheduling.urls')),
    path('quotes/', include('apps.quotes.urls')),
    path('jobs/', include('apps.jobs.urls')),
    path('customers/', include('apps.customers.urls')),
    path('suppliers/', include('apps.suppliers.urls')),
    path('reports/', include('apps.reports.urls')),
    path('invoices/', include('apps.invoices.urls')),
]
