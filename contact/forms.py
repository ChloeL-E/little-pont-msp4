from django import forms
from .models import BookingEnquiry


class BookingEnquiryForm(forms.ModelForm):
    class Meta:
        model = BookingEnquiry
        exclude = ('booking_username', 'date_submitted',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes, and style to form fields. Remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'booking_full_name' : 'Full Name',
            'booking_email' : 'Email',
            'subject' : 'Subject',
            'content' : 'Tell us about your booking request',
        }
        
        # Set autofocus on booking_full_name
        self.fields['booking_full_name'].widget.attrs['autofocus'] = True

        # Customize all fields
        for field_name, field in self.fields.items():
            # Apply CSS classes and styles
            field.widget.attrs['class'] = 'rounded-2'
            field.widget.attrs['style'] = 'border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;'
        
            # Set placeholder text
            if field.required:
                placeholder = f'{placeholders[field_name]} *'
            else:
                placeholder = placeholders[field_name]
            field.widget.attrs['placeholder'] = placeholder
        
            # Hide the label
            field.label = False
