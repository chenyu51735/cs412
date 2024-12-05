from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path(r'profile/<int:pk>', views.ShowProfileView.as_view(), name='project_profile'),
    path(r'', views.ItemListView.as_view(), name='item_list'),
    path(r'item_list', views.ItemListView.as_view(), name='item_list'),
    path(r'item/<int:pk>', views.ItemDetailView.as_view(), name='item'),
    path('login/',auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='project/logged_out.html'), name='logout'),


]