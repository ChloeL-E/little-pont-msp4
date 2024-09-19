from django.shortcuts import render
from instructor.models import Instructor


def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


def cafe(request):
    """A view to return the cafe page"""

    return render(request, "home/cafe.html")
