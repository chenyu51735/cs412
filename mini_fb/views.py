from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import *

# class-based view
class ShowAllProfilesView(ListView):
    '''the view ot show all profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' #this is the context varibale to use the template

class ShowProfilePageView(DetailView):
    '''the view ot show a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'