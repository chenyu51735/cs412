from django.shortcuts import render
import random
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import *

# class-based view
class ShowAllView(ListView):
    '''the view ot show all article'''
    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' #this is the context varibale to use the template

class RandomArticleView(DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"

    def get_object(self):

        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article