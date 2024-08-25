from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from .widgets import DateInput, TimeInput

from .models import Course

class ProductForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        required=False
    )
    end_date = forms.DateField(
        widget=DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        required=False
    )
    start_time = forms.TimeField(
        widget=TimeInput(format='%H:%M'),
        input_formats=['%H:%M'],
        required=False
    )

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize Crispy Forms helper
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='form-control rounded-2'),
            Field('description', css_class='form-control rounded-2'),
            Field('start_date', css_class='form-control datepicker rounded-2'),
            Field('end_date', css_class='form-control datepicker rounded-2'),
            Field('start_time', css_class='form-control timepicker rounded-2'),
            Field('price', css_class='form-control rounded-2'),
            Field('age_group', css_class='form-control rounded-2'),
            Field('instructor', css_class='form-control rounded-2'),
            Submit('submit', 'Save')
        )

        # Define placeholders
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

        # Set placeholder and other attributes for each field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ' rounded-2'
            self.fields[field].widget.attrs['style'] = 'border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;'
        self.fields[field].label = False

        # Set autofocus on the first field
        self.fields['name'].widget.attrs['autofocus'] = True

        # Customizing the choices for 'age_group'
        courses = Course.objects.all()
        course_choices = [("", "Select an Age Group")] + [(course.id, course.age_group) for course in courses]
        self.fields['age_group'].choices = course_choices