from django.contrib import admin
from .models import Instructor

# Register models

class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'instructor_name',
        'bio_description',
        'experience',
        'speciality_age_group',
    )

    ordering = ('instructor_name',)

admin.site.register(Instructor, InstructorAdmin)

# Register your models here.
