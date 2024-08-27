from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='all_courses'),
    path('courses/<str:age_group>/', views.courses_by_age_group, name='courses_by_age_group'),
    path('add/', views.add_course, name='add_course'),
]