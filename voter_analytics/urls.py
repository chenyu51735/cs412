from django.urls import path
from . import views 


urlpatterns = [
    # map the URL (empty string) to the view
    path(r'', views.VotersListView.as_view(), name='home'),
    path(r'voters', views.VotersListView.as_view(), name='voter_list'),
    path(r'voter/<int:pk>', views.ShowVoterView.as_view(), name='voter'),
    path('graphs/', views.VoterGraphsView.as_view(), name='graphs'),
]