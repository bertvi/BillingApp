from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_company', views.create_company, name='create_company'),
    path('list_companies', views.list_companies, name='list_companies'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('list_customers', views.list_customers, name='list_customers'),
    path('create_bill', views.create_bill, name='create_bill'),
    path('<int:bill_id>/', views.detail, name='detail'),
    path('<str:customer_name>/results/', views.results, name='results'),
]