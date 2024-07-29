from django.urls import path
from . import views

urlpatterns = [
    path('', views.babies_courses, name='babies_courses'),
    path('', views.toddlers_courses, name='toddlers_courses'),
    path('', views.preschooler_courses, name='preschooler_courses'),
    path('', views.early_years_courses, name='early_years_courses'),
]