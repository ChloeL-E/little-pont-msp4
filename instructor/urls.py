from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_info, name='instructor_info'),
    path('<instructor_id>', views.instructor_detail, name='instructor_detail'),
    path('add_instructor/', views.add_instructor, name='add_instructor'),
]