from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *


class ShowProfileView(DetailView):
    '''the view to show profile'''
    model = Profile
    template_name = 'project/show_profile.html'
    context_object_name = 'profile' 
