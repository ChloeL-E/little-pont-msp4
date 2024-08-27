from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


def courses_by_age_group(request, age_group):
    """ A view to display courses based on the age group """
    courses = Course.objects.filter(age_group=age_group)
    instructor = Instructor.objects.all()

    # Convert the age group to match the template filename
    template_name = age_group.replace(' ', '_').lower()
    # Handle specific cases
    if template_name == "toddler":
        template_name = "toddlers"

    context = {
        'courses': courses,
        'age_group': age_group,
        'instructor': instructor,
    }
    return render(request, f'products/{template_name}_courses.html', context)


@login_required
def add_course(request):
    """ Add a Course to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site administrators can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('all_courses') 
        else:
            messages.error(request, 'Failed to add course. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """ Edit a course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    course= get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course!')
            return redirect(reverse('all_courses'))
        else:
            messages.error(request, 'Failed to update course. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'products/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    """ Delete a course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'course deleted!')
    return redirect(reverse('all_courses'))
