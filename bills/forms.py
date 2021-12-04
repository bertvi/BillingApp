from django import forms


class CompanyForm(forms.Form):
    name = forms.CharField(label='Company name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    email = forms.CharField(label='E-mail address', max_length=100)
    reg_no = forms.CharField(label='Registration number', max_length=100)
    phone = forms.CharField(label='Phone number', max_length=100)
    iban = forms.CharField(label='Bank account IBAN', max_length=100)
    vat_no = forms.CharField(label='VAT number', max_length=100)


class CustomerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    email = forms.CharField(label='E-mail', max_length=100)
    reg_no = forms.CharField(label='Registration number', max_length=100)
    phone = forms.CharField(label='Phone number', max_length=100)


class BillForm(forms.Form):
    date = forms.DateTimeField(label='Date', max_length=100)
    due_date = forms.DateTimeField(label='Due date', max_length=100)
    reference = forms.CharField(label='Reference number', max_length=100)
    company = forms.CharField(label='Company', max_length=100)
    customer = forms.CharField(label='Customer', max_length=100)
    description = forms.CharField(label='Description', max_length=100)
    invoice_vat = forms.FloatField(label='VAT', max_length=100)
    invoice_total = forms.FloatField(label='Amount total', max_length=100)
