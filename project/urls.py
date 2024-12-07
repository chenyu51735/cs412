from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path(r'project_profile/<int:pk>', views.ShowProfileView.as_view(), name='project_profile'),
    path(r'', views.ItemListView.as_view(), name='item_list'),
    path(r'item_list', views.ItemListView.as_view(), name='item_list'),
    path(r'item/<int:pk>', views.ItemDetailView.as_view(), name='item'),
    path('login/',auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='project/logged_out.html'), name='logout'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/add/<int:pk>/', views.AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('wishlist/remove/<int:pk>/', views.RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),
    path('transaction/complete/<int:pk>/', views.CompleteTransactionView.as_view(), name='complete_transaction'),
    path('item/new/', views.ItemCreateView.as_view(), name='new_item'),
    path('transactions/', views.TransactionHistoryView.as_view(), name='transaction_history'),
    path(r'create_profile', views.CreateProfileView.as_view(), name='create_profile'),
    path('transaction/rate/<int:pk>/', views.RateTransactionView.as_view(), name='rate_transaction'),
    path(r'project_profile/update', views.UpdateProfileView.as_view(), name='update_profile'),  
    path(r'item/<int:pk>/update', views.UpdateItemView.as_view(), name='update_item'),  

]