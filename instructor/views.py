from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Instructor

# Create your views here.

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
    context = {
        'instructor': instructor,
    }
    return render(request, 'instructor/instructor_detail.html', context)