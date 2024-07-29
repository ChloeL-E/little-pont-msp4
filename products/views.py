from django.shortcuts import render
from .models import Course

# Create your views here.

def babies_courses(request):
    """ A view to display all babies courses available """
    babies_courses = Course.objects.filter(age_group='Babies')
    #instructor = Instructor.objects.all()

    context = {
        'courses': babies_courses,
    }
    return render(request, 'products/babies_courses.html', context)


def toddlers_courses(request):
    """ A view to display all toddlers courses available """
    toddlers_courses = Course.objects.filter(age_group='Toddler')
    #instructor = Instructor.objects.all()

    context = {
        'courses': toddlers_courses,
    }
    return render(request, 'products/toddlers_courses.html', context)


def preschooler_courses(request):
    """ A view to display all preschool courses available """
    preschooler_courses = Course.objects.filter(age_group='Preschool')
    #instructor = Instructor.objects.all()

    context = {
        'courses': preschooler_courses,
    }
    return render(request, 'products/preschooler_courses.html', context)


def early_years_courses(request):
    """ A view to display all early years courses available """
    early_years_courses = Course.objects.filter(age_group='Early Years')
    #instructor = Instructor.objects.all()

    context = {
        'courses': early_years_courses,
    }
    return render(request, 'products/early_years_courses.html', context)