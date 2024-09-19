from django.contrib import admin
from .models import Instructor

# Register models


class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "instructor_name",
        "bio_description",
        "experience",
        "speciality_age_group",
        "image",
    )

    ordering = ("id",)


admin.site.register(Instructor, InstructorAdmin)
