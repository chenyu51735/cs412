from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *


class ShowProfileView(DetailView):
    '''the view to show profile'''
    model = Profile
    template_name = 'project/show_profile.html'
    context_object_name = 'profile' 

class ItemListView(ListView):
    '''the view to show items'''
    template_name = 'project/item_list.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 100

    def get_queryset(self):
        """
        Optionally, override this method to filter or order items.
        """
        return super().get_queryset().order_by('-post_date')

class  ItemDetailView(DetailView):
    '''the view to show detail if item'''
    model = Item
    template_name = 'project/item_detail.html'
    context_object_name = 'item'