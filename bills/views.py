from datetime import datetime

from django.http import HttpResponse
from django.template import loader

from bills.models import Billing


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def new(request, data_dict):
    billing = Billing(created=datetime.datetime.now(),
                      changed=None,
                      date=data_dict['date'],
                      due_date=data_dict['due_date'],
                      reference=data_dict['reference'])
    billing.save()

def detail(request, bill_id):
    bill = Billing.objects.get(id=bill_id)
    template = loader.get_template('bills/detail.html')
    context = {
        'bill': bill,
    }
    return HttpResponse(template.render(context, request))

def results(request, customer_name):
    list_of_bills = Billing.objects.all().filter(customer_name=customer_name)
    template = loader.get_template('bills/list.html')
    context = {
        'bills': list_of_bills,
    }
    return HttpResponse(template.render(context, request))
