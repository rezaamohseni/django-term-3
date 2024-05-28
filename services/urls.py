from django.urls import path
from .views import *


app_name = 'services'

urlpatterns = [
    path('', services, name='services'),
    path('<str:category>', services, name='list_by_category'),
    path('service-detail/', services_detail, name='services-detail'),
    path('qoute/', qoute, name='qoute'),
]
