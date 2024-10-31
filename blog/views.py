from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.request import HttpRequest as HttpRequest
from django.shortcuts import render
import random
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from typing import Any
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView
from .forms import *
from .models import *
from django.urls import reverse
# class-based view
from .forms import CreateArticleForm, CreateCommentForm ## new import


class ShowAllView(ListView):
    '''the view ot show all article'''
    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' #this is the context varibale to use the template
    def dispatch(self, *args: Any, **kwargs: Any):
        return super().dispatch(*args, **kwargs)
    
class RandomArticleView(DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"

    def get_object(self):

        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article

class CreateCommentView(CreateView):

    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['article'] = article
        return context
    
    def get_success_url(self) -> str:
        '''Return the URL to redirect to on success'''
        # return reverse('show_all')
        article = Article.objects.get(pk=self.kwargs['pk'])
        return reverse('article', kwargs={'pk':article.pk})
    
    def form_valid(self, form):
        '''This method is callled after the form is validated, 
        before saving data to the database
        ''' 
        print(f'CreateCommentView.form_valid(): form={form.cleaned_data}')
        print(f'CreateCommentView.form_valid(): self.kwargs={self.kwargs}')

        article = Article.objects.get(pk=self.kwargs['pk'])

        form.instance.article = article
        return super().form_valid(form)

class CreateArticleView(CreateView):
    '''A view to create a new Article and save it to the database.'''
    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"
    def form_valid(self, form):
        '''
        Handle the form submission to create a new Article object.
        '''
        print(f'CreateArticleView.form_valid(): form.cleaned_data={form.cleaned_data}')
        # delegate work to the superclass version of this method
        return super().form_valid(form)