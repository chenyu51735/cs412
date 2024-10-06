## hw/urls.py
## description: URL patterns for the hw app

from django.urls import path
from django.conf import settings
from . import views
from .views import ShowAllView
# all of the URLs that are part of this app
urlpatterns = [
    path(r'', ShowAllView.as_view(), name='show_all'),
]