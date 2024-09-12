import logging
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import BookingEnquiry
from .forms import BookingEnquiryForm


logger = logging.getLogger('contact')


@login_required
def send_booking_enquiry(request):
    """Allow the user to send a party booking enquiry to the site manager"""
    form = BookingEnquiryForm()
    
    if request.method == 'POST':
        form = BookingEnquiryForm(request.POST)
        if form.is_valid():
            # Log form data retrieval
            logger.info(f"Form is valid. User: {request.user.username} submitting booking enquiry.")
            # Get the form data
            full_name = form.cleaned_data['booking_full_name']
            email = form.cleaned_data['booking_email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            
            # get the logged in users' username using fk link to UserProfile
            user_profile = request.user.userprofile
            
            # Log that user profile is being used
            logger.info(f"Booking enquiry for user profile: {user_profile} with email: {email}")
            
          # Create and save the BookingEnquiry to the database
            try:
                booking_enquiry = BookingEnquiry.objects.create(
                    booking_username=user_profile,
                    booking_full_name=full_name,
                    booking_email=email,
                    subject=subject,
                    content=content
                )
                logger.info(f"BookingEnquiry object created for user: {request.user.username}")
            except Exception as e:
                logger.error(f"Error creating BookingEnquiry object: {e}")
                messages.error(request, "There was an issue saving your booking enquiry. Please try again.")
                return redirect('send_booking_enquiry')

            # set the email subject and content
            email_subject = render_to_string(
                "contact/contact_confirmation_emails/contact_confirmation_email_subject.txt",
                {"contact": booking_enquiry}
            ).strip()
            email_body = render_to_string(
                "contact/contact_confirmation_emails/contact_confirmation_email.txt",
                {"contact": booking_enquiry, "contact_email": settings.DEFAULT_FROM_EMAIL}
            )
            # attempt to send email to user
            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [booking_enquiry.booking_email],
                )
                logger.info(f"Email sent to {booking_enquiry.booking_email} for booking enquiry {booking_enquiry.id}")
                messages.success(request, "Thank you for sending a party booking enquiry! We aim to respond within 2 working days.")
                return redirect('home')  # Success message and redirect to home
            # Log the exception or handle it as necessary
            except Exception as e:
                logger.error(f"Error sending email to {booking_enquiry.booking_email}: {e}")
                messages.error(request, f"Sorry, your booking enquiry couldn't be sent due to: {e}. Please ensure you have completed the form correctly and submit again. Thank you") 
                return redirect('send_booking_enquiry')          

    context = {
        'form': form,
    }

    return render(request, 'contact/party_booking.html', context)
