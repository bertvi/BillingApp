from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_company', views.create_company, name='create_company'),
    path('create_bill', views.create_bill, name='create_bill'),
    path('list_companies', views.list_companies, name='list_companies'),
    path('<int:bill_id>/', views.detail, name='detail'),
    path('<str:customer_name>/results/', views.results, name='results'),
]