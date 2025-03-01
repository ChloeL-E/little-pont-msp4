from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "town_or_city": "Town or City",
            "county": "County, State or Locality",
            "postcode": "Postal Code",
        }
        # set form autofocus
        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:  # handle placeholders and remove labels
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
        
        self.fields["full_name"].widget.attrs["aria-label"] = "Full Name"
        self.fields["email"].widget.attrs["aria-label"] = "Email Address"
        self.fields["phone_number"].widget.attrs["aria-label"] = (
            "Phone Number")
        self.fields["street_address1"].widget.attrs["aria-label"] = (
            "Street Address 1")
        self.fields["street_address2"].widget.attrs["aria-label"] = (
            "Street Address 2")
        self.fields["town_or_city"].widget.attrs["aria-label"] = (
            "Town or City")
        self.fields["county"].widget.attrs["aria-label"] = (
            "County, State or Locality")
        self.fields["postcode"].widget.attrs["aria-label"] = "Postal Code"
        self.fields["country"].widget.attrs["aria-label"] = "Country"
