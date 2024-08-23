from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from instructor.models import Instructor
from .models import Course
from .forms import ProductForm

# Create your views here.

def all_courses(request):
    """ A view to display all the courses available """

    courses = Course.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                courses = courses.annotate(lower_name=Lower('name'))
            if sortkey == 'age_group':
                sortkey = 'age_group'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            courses = courses.order_by(sortkey)

    context = {
        'courses': courses,
    }

    return render(request, 'products/all_courses.html', context)
    """ A view to display all the courses available """


def courses_by_age_group(request, age_group):
    """ A view to display courses based on the age group """
    courses = Course.objects.filter(age_group=age_group)
    instructor = Instructor.objects.all()

    # Convert the age group to match the template filename
    template_name = age_group.replace(' ', '_').lower()
    # Handle specific cases
    if template_name == "preschool":
        template_name = "preschooler"
    if template_name == "toddler":
        template_name = "toddlers"

    context = {
        'courses': courses,
        'age_group': age_group,
        'instructor': instructor,
    }
    return render(request, f'products/{template_name}_courses.html', context)


def add_product(request):
    """ Add a Course to the site """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)