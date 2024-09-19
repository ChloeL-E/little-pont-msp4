from django import forms

# from instructor.models import Instructor
from .models import Course
from .widgets import DateInput, TimeInput


# setting date input type
class DateInput(forms.DateInput):
    input_type = "date"


# setting time input type
class TimeInput(forms.TimeInput):
    input_type = "time"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        # adding date/time pickers to relevent fields
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
            "start_time": TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        courses = Course.objects.all()  # Get all courses
        # course_choices = [("  ")] + [
        # (course.id, course.age_group) for course in courses
        # ]

        # Get the age_group values and set them as choices
        age_group_set = set(
            courses.values_list("age_group", flat=True)
        )  # Use a set to get each unique age group
        age_group_choices = [("", "Select an Age Group")] + [
            (age_group, dict(Course.AGE_GROUP)[age_group])
            for age_group in age_group_set
        ]
        self.fields["age_group"].choices = age_group_choices

        # form field styling
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "rounded-2"
            field.widget.attrs["style"] = (
                "border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;"
            )

        # naming placeholders
        placeholders = {
            "name": "Course Name",
            "description": "Course Description",
            "start_date": "Start Date",
            "end_date": "End Date",
            "start_time": "Course Start Time",
            "price": "Price",
            "age_group": "Age Group",
            "instructor": "Lead Instructor",
        }

        # autofocus to 'name' input field
        # adding * to required input placeholders and removing labels
        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
                self.fields[field].label = False
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
