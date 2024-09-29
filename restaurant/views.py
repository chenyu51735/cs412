from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest, HttpResponse
import time
from datetime import datetime, timedelta
import random

special = ["Steamed Lobster $3.99",
           "Steamed Egg $3.99",
           "Steamed Salmon $3.99",
           "Steamed Turkey $3.99"]
def base(request):
    '''
    Function to handle the URL request for /restaurant
    Delegate rendering to the template restaurant/templates/base.html.
    '''

    template_name = 'restaurant/base.html'
    #create a dictionary of context varibales for the template:
    return render(request, template_name)

def main(request):
    '''
    Function to handle the URL request for /restaurant
    Delegate rendering to the template restaurant/templates/main.html.
    '''

    template_name = 'restaurant/main.html'
    #create a dictionary of context varibales for the template:
    return render(request, template_name)



def order(request):
    '''
    Function to handle the URL request for /restaurant
    Delegate rendering to the template restaurant/templates/order.html.
    '''

    template_name = 'restaurant/order.html'
    #create a dictionary of context varibales for the template:
    daily_special = random.choice(special)
    context = {
        'daily_special': daily_special
    }
    return render(request, template_name, context)

def confirmation(request):
    '''
    Handle the form submission.
    Read the form data from the request,
    and send it back to a template.
    '''

    template_name = 'restaurant/confirmation.html'
    # print(request)
    
    # check that we have a POST request
    if request.POST:

        # print(request.POST)
        # read the form data into python variables
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        instructions = request.POST.get('instructions')
        menu_items = {
            "Steamed Pork": 2.99,
            "Steamed Beef": 2.99,
            "Steamed Chicken": 2.99,
            "Steamed Vegen": 1.99,
            "Daily Special": 3.99
        }
        # package the form data up as context variables for the template

        ordered_items = []
        total_price = 0.0
        for item, price in menu_items.items():
            if request.POST.get(item):
                ordered_items.append(item)
                total_price += price

        ready_time = datetime.now() + timedelta(minutes=random.randint(30, 60))
        ready_time_str = ready_time.strftime("%H:%M")

        context = {
            'customer_name': name,
            'customer_phone': phone,
            'customer_email': email,
            'special_instructions': instructions,
            'ordered_items': ordered_items,
            'total_price': total_price,
            'ready_time': ready_time_str
        }

        return render(request, template_name, context)
    return redirect("order")