from django.urls import path
from . import views

urlpatterns = [
    path('instructor/<int:id>/', views.instructor_info, name='instructor_info')
]