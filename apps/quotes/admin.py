from django.contrib import admin

from .models import Quote

class QuoteAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None,               {'fields': ['customer', 'customer_order_number', 'status', 'subtotal']}),
        ('Date information', {'fields': ['ordered_date', 'delivery_due_date']}),
    ]    
    list_display = ('customer', 'customer_order_number', 'status', 'subtotal', 'created', 'ordered_date', 'delivery_due_date')
    list_filter = [ 'created', 'ordered_date', 'delivery_due_date']
    search_fields = ['customer', 'customer_order_number', 'status']


admin.site.register(Quote, QuoteAdmin)