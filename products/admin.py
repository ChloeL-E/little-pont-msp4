from django.contrib import admin
from .models import Course

# Register models

class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age_group',
        'start_date',
        'end_date',
        'start_time',
        'price'
    )

    ordering = ('start_date',)

admin.site.register(Course, CourseAdmin)
