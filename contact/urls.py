from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_booking_enquiry, name='send_booking_enquiry'),
]