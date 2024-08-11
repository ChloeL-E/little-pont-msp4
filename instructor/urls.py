from django.urls import path
from . import views

urlpatterns = [
    path('instructor_one/', views.instructor_one, name='instructor_one'),
    path('instructor_two/', views.instructor_two, name='instructor_two'),
    path('instructor_three/', views.instructor_three, name='instructor_three'),
    path('instructor_four/', views.instructor_four, name='instructor_four'),
]