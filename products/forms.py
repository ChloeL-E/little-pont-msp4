from django import forms

from instructor.models import Instructor
from .models import Course


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'start_time': TimeInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instructor_name = Instructor.objects.all() # Fetch all instructors
        courses = Course.objects.all()  # Fetch all courses
        course_choices = [("  ")] + [(course.id, course.age_group) for course in courses]

        self.fields['age_group'].choices = course_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-2'
            field.widget.attrs['style'] = 'border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;'
       
        placeholders = {
            'name': 'Course Name',
            'description': 'Course Description',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'start_time': 'Course Start Time',
            'price': 'Price',
            'age_group': 'Age Group',
            'instructor': 'Lead Instructor',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
                self.fields[field].label = False
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            