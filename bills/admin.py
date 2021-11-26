from django.contrib import admin

from .models import Company, Customer, Billing

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Billing)