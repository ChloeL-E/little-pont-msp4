from django.urls import path
from . import views

urlpatterns = [
    path("", views.instructor_info, name="instructor_info"),
    path(
        "instructor_detail/<instructor_id>/",
        views.instructor_detail,
        name="instructor_detail",
    ),
    path("add_instructor/", views.add_instructor, name="add_instructor"),
    path(
        "edit_instructor/<int:instructor_id>/",
        views.edit_instructor,
        name="edit_instructor",
    ),
    path(
        "delete_instructor/<int:instructor_id>/",
        views.delete_instructor,
        name="delete_instructor",
    ),
]
