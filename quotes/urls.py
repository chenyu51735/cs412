## quotes/urls.py
## description: URL patterns for the quotes app

from django.urls import path
from django.conf import settings
from . import views

# all of the URLs that are part of this app
urlpatterns = [
    path('quote', views.quote, name="quote"),
    path(r'', views.home, name="home"),
    path('about', views.about, name="about"),
    path('show_all', views.show_all, name="show_all"),   
    path('base', views.base, name="base"),   
     
    
]