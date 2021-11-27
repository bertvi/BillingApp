from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bill_id>/', views.detail, name='detail'),
    path('<string:customer_name>/results/', views.results, name='results'),
]