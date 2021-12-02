import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from bills.forms import CompanyForm, BillForm
from bills.models import Billing, Company


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, bill_id):
    try:
        bill = Billing.objects.get(id=bill_id)
        template = loader.get_template('bills/detail.html')
        context = {
            'bill': bill,
        }
    except Billing.DoesNotExist:
        raise Http404("Bill does not exist")

    return HttpResponse(template.render(context, request))


def results(request, customer_name):
    list_of_bills = Billing.objects.all().filter(customer_name=customer_name)
    template = loader.get_template('bills/list.html')
    context = {
        'bills': list_of_bills,
    }
    return HttpResponse(template.render(context, request))


def create_company(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            save_company(form.data)
            template = loader.get_template('bills/company/saved.html')
            return HttpResponse(template.render({}, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CompanyForm()

    return render(request, 'company/company.html', {'form': form})


def save_company(data):
    company = Company(created=datetime.datetime.now(),
                      changed=datetime.datetime.now(),
                      name=data.get('name'),
                      address=data.get('address'),
                      email=data.get('email'),
                      reg_no=data.get('reg_no'),
                      phone=data.get('phone'),
                      iban=data.get('iban'),
                      vat_no=data.get('vat_no'))
    company.save()


def list_companies(request):
    try:
        companies = Company.objects.all()
        template = loader.get_template('company/view.html')
        context = {
            'companies': companies,
        }
    except Company.DoesNotExist:
        raise Http404("No companies found")

    return HttpResponse(template.render(context, request))


def create_bill(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BillForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            save_bill(form.data)
            template = loader.get_template('bills/bills/saved.html')
            return HttpResponse(template.render({}, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BillForm()

    return render(request, 'bills/bill.html', {'form': form})


def save_bill(data):
    bill = Billing(created=datetime.datetime.now(),
                   changed=datetime.datetime.now(),
                   date=data.get('date'),
                   due_date=data.get('due_date'),
                   reference=data.get('reference'),
                   company=data.get('company'),
                   customer=data.get('customer'),
                   description=data.get('description'),
                   invoice_vat=data.get('invoice_vat'),
                   invoice_total=data.get('invoice_total'))
    bill.save()
