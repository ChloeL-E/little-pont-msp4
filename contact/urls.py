from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_enquiry, name='booking_enquiry'),
]