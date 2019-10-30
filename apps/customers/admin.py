from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None,               {'fields': ['customer_name', 'abn', 'credit_limit', 'status']}),
    ]    
    list_display = ('customer_name', 'abn', 'credit_limit', 'status')
    list_filter = [ 'customer_name', 'abn', 'status']
    search_fields = ['customer_name', 'abn', 'status']

admin.site.register(Customer, CustomerAdmin)