from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from products.models import Course

# Create your views here.

def view_bag(request):
    """ A view to render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the course to the shopping bag """

    course = get_object_or_404(Course, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        #messages.success(
                #request, (f"You have added another {course.name} to your bag")
            #)
    else:
        bag[item_id] = quantity
        #messages.success(
                #request, (f"{course.name} has been added to your bag")
            #)

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust course quantities in the shopping bag """

    course = get_object_or_404(Course, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        #messages.success(
            #request, f"Updated {course.name} quantity to {bag[item_id]}!"
            #)
    else:
        bag.pop(item_id, None)
        # messages.info(request, f"{course.name} has been removed from your bag.")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    course = get_object_or_404(Course, pk=item_id)
    try:

        bag = request.session.get("bag", {})

        bag.pop(item_id)
        # messages.success(request, f"Removed {course.name} from your bag!")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        # messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)