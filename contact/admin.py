from django.contrib import admin
from .models import BookingEnquiry

# Register models

class BookingEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'booking_username',
        'booking_full_name',
        'booking_email',
        'subject',
        'content',
        'date_submitted',
    )

    ordering = ('-date_submitted',)

admin.site.register(BookingEnquiry, BookingEnquiryAdmin)