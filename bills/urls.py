from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /bills/5/
    path('<int:bill_id>/', views.detail, name='detail'),
    # ex: /bills/microsoft/results/
    path('<string:customer_name>/results/', views.results, name='results'),
]