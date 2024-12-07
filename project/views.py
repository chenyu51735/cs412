from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import login

class ShowProfileView(DetailView):
    '''the view to show profile'''
    model = Profile
    template_name = 'project/show_profile.html'
    context_object_name = 'project_profile' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.get_items()
        return context
    
class ItemListView(ListView):
    '''The view to show items'''
    template_name = 'project/item_list.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 100

    def get_queryset(self):
        """
        Return items based on search query and filters.
        """
        queryset = super().get_queryset().filter(sold=False).order_by('-post_date')

        # Search query
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(
                models.Q(title__icontains=query) |
                models.Q(brand__icontains=query) |
                models.Q(description__icontains=query)
            )

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add extra context for filters.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Item.Category.choices
        return context
class  ItemDetailView(DetailView):
    '''the view to show detail if item'''
    model = Item
    template_name = 'project/item_detail.html'
    context_object_name = 'item'


class WishlistView(ListView):
    '''View to display user's wishlist'''
    model = Wishlist
    template_name = 'project/wishlist.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        return Wishlist.objects.filter(profile=self.request.user.project_profile)

class AddToWishlistView(View):
    '''Add item to user's wishlist'''
    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        profile = request.user.project_profile
        Wishlist.objects.get_or_create(profile=profile, item=item)
        return redirect('wishlist')

class RemoveFromWishlistView(View):
    '''Remove item from user's wishlist'''
    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        wishlist_item = get_object_or_404(Wishlist, pk=pk)
        if wishlist_item.profile == request.user.project_profile:
            wishlist_item.delete()
        return redirect('wishlist')
    
class CompleteTransactionView(View):
    '''Complete a transaction for an item'''
    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        buyer = request.user.project_profile
        if item.seller == buyer:
            return redirect('item_list')
        Transaction.objects.create(item=item, buyer=buyer)
        item.delete()
        return redirect('item_list')

class ItemCreateView(CreateView):
    '''View to post a new item'''
    model = Item
    fields = ['title', 'product', 'description', 'brand', 'category', 'condition', 'price', 'images']
    template_name = 'project/item_form.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user.project_profile
        return super().form_valid(form)
    
class TransactionHistoryView(LoginRequiredMixin, ListView):
    """View to show items the user has sold and bought"""
    template_name = 'project/transaction_history.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        profile = self.request.user.project_profile
        sold_items = Transaction.objects.filter(item__seller=profile)
        bought_items = Transaction.objects.filter(buyer=profile)
        return {
            'sold_items': sold_items,
            'bought_items': bought_items,
        }
    
class CreateProfileView(CreateView):
    '''the view to create profile'''
    model = Profile
    fields = ['first_name', 'last_name', 'city', 'email', 'image_file', 'bio']
    template_name = 'project/create_profile_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_creation_form'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        user_creation_form = UserCreationForm(self.request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save()
            if Profile.objects.filter(user=user).exists():
                return redirect('project_profile', pk=user.project_profile.pk)
            login(self.request, user)
            form.instance.user = user
            
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, user_creation_form=user_creation_form))

class RateTransactionView(View):
    '''View to handle rating a transaction'''
    def post(self, request, pk, *args, **kwargs):
        transaction = get_object_or_404(Transaction, pk=pk)
        profile = request.user.project_profile

        # Ensure the logged-in user is part of the transaction
        if transaction.buyer != profile and transaction.item.seller != profile:
            messages.error(request, "You are not authorized to rate this transaction.")
            return redirect('transaction_history')

        try:
            # Get the rating value from the form
            rating = int(request.POST.get('rating'))
            if rating < 1 or rating > 5:
                raise ValidationError("Rating must be between 1 and 5.")

            # Update the appropriate rating field
            if profile == transaction.item.seller:
                transaction.buyer_rating = rating
                transaction.save()
                transaction.buyer.update_rating()
                messages.success(request, "Successfully rated the buyer.")
            elif profile == transaction.buyer:
                transaction.seller_rating = rating
                transaction.save()
                transaction.item.seller.update_rating()
                messages.success(request, "Successfully rated the seller.")

        except (ValueError, ValidationError) as e:
            messages.error(request, str(e))

        # Redirect to the transaction history page
        return redirect('transaction_history')
    
class CompleteTransactionView(View):
    '''Complete a transaction for an item'''
    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        buyer = request.user.project_profile

        # Prevent buying your own item
        if item.seller == buyer:
            return redirect('item_list')

        # Create the transaction
        transaction = Transaction.objects.create(item=item, buyer=buyer)

        # Mark the item as sold
        item.sold = True
        item.save()

        # Get the redirect URL and replace 'pk=0' with the actual transaction ID
        redirect_url = request.POST.get('redirect_to', 'item_list')
        redirect_url = redirect_url.replace('pk=0', f'pk={transaction.pk}')
        return redirect(redirect_url)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['city', 'email', 'image_file', 'phone', 'bio'] 
    template_name = 'project/update_profile.html'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'UpdateProfileView.form_valid(): form={form.cleaned_data}')
        print(f'UpdateProfileView.form_valid(): self.kwargs={self.kwargs}')

        user = self.request.user
        print(f"UpdateProfileView user={user} profile.user={user}")
        form.instance.user = user
        return super().form_valid(form)

class UpdateItemView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['product', 'title', 'category', 'brand', 'description', 'condition', 'price', 'images'] 
    template_name = 'project/update_item.html'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 

    def get_objects(self):
        return Item.objects.get(user=self.request.user)

    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'UpdateProfileView.form_valid(): form={form.cleaned_data}')
        print(f'UpdateProfileView.form_valid(): self.kwargs={self.kwargs}')

        user = self.request.user
        print(f"UpdateProfileView user={user} profile.user={user}")
        form.instance.user = user
        return super().form_valid(form)
    