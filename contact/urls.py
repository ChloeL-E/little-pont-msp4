from django.urls import path
from . import views

urlpatterns = [
    path('send-booking-enquiry/', views.send_booking_enquiry, name='send_booking_enquiry'),
]