from django.db import models

class Company(models.Model):
    created = models.DateTimeField('created')
    changed = models.DateTimeField('changed')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    vat_no = models.CharField(max_length=255)

class Customer(models.Model):
    created = models.DateTimeField('created')
    changed = models.DateTimeField('changed')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Billing(models.Model):
    created = models.DateTimeField('created')
    changed = models.DateTimeField('changed')
    date = models.DateTimeField('date')
    due_date = models.DateTimeField('due date')
    reference = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.JSONField(max_length=1000)
    invoice_vat = models.FloatField(max_length=20)
    invoice_total = models.FloatField(max_length=20)
