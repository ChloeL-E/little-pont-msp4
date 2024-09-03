from django.db import models
from profiles.models import User

from django.utils import timezone


class BookingEnquiry(models.Model):
    """
    A model to set up the Booking Enquiry Form. User model as fk
    """
    booking_username = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE, related_name='booking')
    booking_full_name = models.CharField(max_length=50, null=False, blank=False)
    booking_email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date_submitted = models.DateTimeField(default=timezone.now, editable=False)
    
    class Meta:
        ordering = ["-date_submitted"]
    
    def __str__(self):
        """Return the full name and email as its string representation."""
        return f"{self.booking_full_name} ({self.booking_email})"
    