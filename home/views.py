from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to returnt he index page """

    return render(request, 'home/index.html')