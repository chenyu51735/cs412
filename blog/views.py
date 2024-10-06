from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import *

# class-based view
class ShowAllView(ListView):
    '''the view ot show all article'''
    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' #this is the context varibale to use the template