## hw/urls.py
## description: URL patterns for the hw app

from django.urls import path
from django.conf import settings
from . import views
from .views import ShowAllView, CreateArticleView
from django.contrib.auth import views as auth_views
from .views import *
# all of the URLs that are part of this app
urlpatterns = [
    path(r'show_all', views.ShowAllView.as_view(), name='show_all'),
    path(r'', views.RandomArticleView.as_view(), name='article'),
    path(r'article/<int:pk>', views.RandomArticleView.as_view(), name='article'),
    path(r'article/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path('create_article', CreateArticleView.as_view(), name='create_article'), 
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='show_all'), name='logout'),
]