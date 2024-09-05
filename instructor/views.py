from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import InstructorForm

from .models import Instructor
from products.models import Course


def instructor_info(request):
    """ A view to display all instrcutors """
    
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors,
    }
    return render(request, 'instructor/instructor_info.html', context)


def instructor_detail(request, instructor_id):
    """ A view to display details of a specific instructor """
    
    instructor = get_object_or_404(Instructor, pk=instructor_id)

    # Retrieve courses based on the instructor's age group
    courses = Course.objects.filter(age_group=instructor.speciality_age_group)

    context = {
        'instructor': instructor,
        'courses': courses,
    }
    return render(request, 'instructor/instructor_detail.html', context)

@login_required
def add_instructor(request):
    """ A view to allow admin to add a new instructor """
    
    if not request.user.is_superuser:
        messages.error(request, "We're sorry but only administrators can do that.")
        return redirect("home")
    
    if request.method == "POST":
        form = InstructorForm(request.POST, request.FILES)  # if an image atached
        if form.is_valid():
            instructor = form.save()
            messages.success(request, "Successfully added a new member to our team!")
            return redirect(reverse('instructor_detail', args=[instructor.id]))
        else:
            messages.error(
                request, "Sorry! You failed to add a new instructor. \
                Please ensure the form is valid."
            )
    else:
        form = InstructorForm()

    template = "instructor/add_instructor.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def edit_instructor(request, instructor_id):
    """ Edit a course """
    
    instructor= get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated instructor!')
            return redirect(reverse('instructor_detail', args=[instructor.id]))
        else:
            messages.error(request, 'Failed to update instructor. Please ensure the form is valid.')
    else:
        form = InstructorForm(instance=instructor)
        messages.info(request, f'You are editing {instructor.instructor_name}')

    template = 'instructor/edit_instructor.html'
    context = {
        'form': form,
        'instructor': instructor,
    }

    return render(request, template, context)


def delete_instructor(request, instructor_id):
    """ Delete an instructor """
    
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    instructor.delete()
    messages.success(request, 'Instructor deleted!')
    return redirect(reverse('instructor_info'))