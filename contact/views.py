from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import BookingEnquiry
from .forms import BookingEnquiryForm


@login_required
def send_booking_enquiry(request):
    """Allow the user to send a party booking enquiry to the site manager"""
    if request.method == 'POST':
        form = BookingEnquiryForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get("full_name")
            booking_email = request.POST.get("booking_email")
            subject = request.POST.get("subject")
            content = request.POST.get("content")
            contact = form.save()
            user_email = email
            email_subject = render_to_string(
                "contact/contact_confirmation_emails/contact-email-subject.txt",
                {"contact": contact}
            ).strip()
            email_body = render_to_string(
                "contact/contact_confirmation_emails/contact-confirmation-email.txt",
                {"contact": contact, "contact_email": settings.DEFAULT_FROM_EMAIL}
            )

            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [user_email]
                )
                messages.success(request, "Thank you for sending a party booking enquiry! We aim to respond within 2 working days.")
                return redirect('home')  # Redirect to home
            except Exception as e:
                messages.error(request, "Sorry, there was an error sending your enquiry. Please try again later.")
                # Log the exception or handle it as necessary
        else:
            messages.error(request, "Sorry, your booking enquiry couldn't be sent. Please ensure you have completed the form correctly and submit again. Thank you")
    else:
        form = BookingEnquiryForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/party_booking.html', context)