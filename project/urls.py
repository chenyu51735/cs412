from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'profile/<int:pk>', views.ShowProfileView.as_view(), name='show_profile'),


]