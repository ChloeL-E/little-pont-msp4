from django.urls import path
from . import views

urlpatterns = [
    path('babies/', views.babies_courses, name='babies_courses'),
    path('toddlers/', views.toddlers_courses, name='toddlers_courses'),
    path('preschooler/', views.preschooler_courses, name='preschooler_courses'),
    path('early_years/', views.early_years_courses, name='early_years_courses'),
    path('add/', views.add_product, name='add_product'),
]