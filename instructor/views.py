from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render
from .models import Instructor

# Create your views here.

def instructor_one(request):
    """ A view to display instructor ones info """
    instructor_one = get_object_or_404(Instructor, pk=1)

    context = {
        'instructor': instructor_one,
    }
    return render(request, 'instructor/instructor_info.html', context)


def instructor_two(request):
    """ A view to display instructor twos info """
    instructor_two = get_object_or_404(Instructor, pk=2)

    context = {
        'instructor': instructor_two,
    }
    return render(request, 'instructor/instructor_info.html', context)


def instructor_three(request):
    """ A view to display instructor threes info """
    instructor_three = get_object_or_404(Instructor, pk=3)

    context = {
        'instructor': instructor_three,
    }
    return render(request, 'instructor/instructor_info.html', context)


def instructor_four(request):
    """ A view to display instructor fours info """
    instructor_four = get_object_or_404(Instructor, pk=4)

    context = {
        'instructor': instructor_four,
    }
    return render(request, 'instructor/instructor_info.html', context)
