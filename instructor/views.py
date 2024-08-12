from django.shortcuts import render, get_object_or_404
from .models import Instructor

# Create your views here.

def instructor_info(request, id):
    """ A view to display instructor details based on the given id """
    instructor = get_object_or_404(Instructor, pk=id)
    context = {
        'instructor': instructor,
    }
    return render(request, 'instructor/instructor_info.html', context)
