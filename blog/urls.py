## hw/urls.py
## description: URL patterns for the hw app

from django.urls import path
from django.conf import settings
from . import views
from .views import ShowAllView, CreateArticleView
# all of the URLs that are part of this app
urlpatterns = [
    path(r'show_all', views.ShowAllView.as_view(), name='show_all'),
    path(r'', views.RandomArticleView.as_view(), name='article'),
    path(r'article/<int:pk>', views.RandomArticleView.as_view(), name='article'),
    path(r'article/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path('create_article', CreateArticleView.as_view(), name='create_article'), 
]