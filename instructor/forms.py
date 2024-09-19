from django import forms
from .widgets import CustomClearableFileInput

from .models import Instructor


class InstructorForm(forms.ModelForm):
    """A form to add a new instructor"""

    class Meta:
        model = Instructor
        fields = "__all__"  # display all fields

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # set the placeholders
        placeholders = {
            "instructor_name": "Instructors Name",
            "bio_description": "Bio Description",
            "experience": "Experience",
            "speciality_age_group": "Speciality Age Group",
            "image_url": "Image URL",
            "image": "Image",
        }

        self.fields["instructor_name"].widget.attrs[
            "autofocus"
        ] = True  # autofocus on instructor name field
        for field_name, field in self.fields.items():  # style the input boxes
            field.widget.attrs["class"] = "rounded-2"
            field.widget.attrs["style"] = (
                "border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;"
            )
        # set the placeholders and remove any input labels
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
                self.fields[field].label = False
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
