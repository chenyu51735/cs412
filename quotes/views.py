from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random
# Create your views here.

## global list for quotes
quotes = [
          "My mother often said, as long as a person is happy at work, then poverty is nothing to be ashamed of.",
          "We survive in adversity and perish in ease and comfort.",
          "The timid die of hunger, the bold of overeating.",
          ]

## global list for URLs of images
images = ["https://u.osu.edu/mclc/files/2014/11/yuhua2-rre64k.jpg",
          "https://www.chinafile.com/sites/default/files/assets/images/article/featured/yu-hua-4.jpg",
          "https://static01.nyt.com/images/2011/11/13/books/review/13MISHAN/13MISHAN-articleLarge.jpg?quality=75&auto=webp&disable=upscale",
         ]


def quote(request):
    '''
    Function to handle the URL request for /quotes
    Delegate rendering to the template quotes/templates/quote.html.
    '''

    template_name = 'quote.html'
    #create a dictionary of context varibales for the template:
    context = {
        "rand_images" : random.choice(images),
        "rand_quotes" : random.choice(quotes),
    }
    return render(request, template_name, context)

def about(request):
    '''
    Function to handle the URL request for /quote
    Delegate rendering to the template quotes/templates/quote.html.
    '''

    template_name = 'about.html'
    #create a dictionary of context varibales for the template:
    context = {
        "rand_images" : random.choice(images),
        "rand_quotes" : random.choice(quotes),
    }
    return render(request, template_name, context)

def show_all(request):
    '''
    Function to handle the URL request for /quote
    Delegate rendering to the template quotes/templates/quote.html.
    '''

    template_name = 'show_all.html'
    #create a dictionary of context varibales for the template:
    context = {
        "images_0" : images[0],
        "images_1" : images[1],
        "images_2" : images[2],
        "quotes_0" : quotes[0],
        "quotes_1" : quotes[1],
        "quotes_2" : quotes[2],
    }
    return render(request, template_name, context)

def base(request):
    '''
    Function to handle the URL request for /quote
    Delegate rendering to the template quotes/templates/quote.html.
    '''

    template_name = 'base.html'
    #create a dictionary of context varibales for the template:
    context = {
        "rand_images" : random.choice(images),
        "rand_quotes" : random.choice(quotes),
    }
    return render(request, template_name, context)

def home(request):
    '''
    Function to handle the URL request for /quote
    Delegate rendering to the template quotes/templates/quote.html.
    '''

    template_name = 'home.html'
    #create a dictionary of context varibales for the template:
    context = {
        "rand_images" : random.choice(images),
        "rand_quotes" : random.choice(quotes),
    }
    return render(request, template_name, context)