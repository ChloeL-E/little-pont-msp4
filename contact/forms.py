from django import forms
from .models import BookingEnquiry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class BookingEnquiryForm(forms.ModelForm):
    class Meta:
        model = BookingEnquiry
        exclude = (
            "booking_username",
            "date_submitted",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes, and style to form fields.
        sr-only classes added to form fields.
        Remove auto-generated labels and set autofocus on first field
        """
        super(BookingEnquiryForm, self).__init__(*args, **kwargs)

        # Define placeholders for the fields
        placeholders = {
            "booking_full_name": "Full Name",
            "booking_email": "Email",
            "subject": "Subject",
            "content": "Tell us about your booking request",
        }

        # Initialize Crispy FormHelper for layout customization
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Apply 'sr-only' class to labels for screen readers
            Field('booking_full_name', css_class="sr-only"),
            Field('booking_email', css_class="sr-only"),
            Field('subject', css_class="sr-only"),
            Field('content', css_class="sr-only"),
        )
        # Set autofocus on name
        self.fields["booking_full_name"].widget.attrs["autofocus"] = True
        for field_name, field in self.fields.items():
            # Apply CSS classes and styles
            field.widget.attrs["class"] = "rounded-2"
            field.widget.attrs["style"] = (
                "border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;"
            )
            # Set placeholder text
            if field.required:
                placeholder = f"{placeholders[field_name]} *"
            else:
                placeholder = placeholders[field_name]
            field.widget.attrs["placeholder"] = placeholder
