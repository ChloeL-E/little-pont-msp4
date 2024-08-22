from django import forms
from .models import Course
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        courses = Course.objects.all()  # Fetch all courses
        course_choices = [(course.id, course.name) for course in courses]

        self.fields['course'].choices = course_choices  # Assuming 'course' is the field name in the Product model
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-2'
            field.widget.attrs['style'] = 'border: 1px solid #ffe6f2; box-shadow: 0 1px 3px 0 #ffe6f2;'
