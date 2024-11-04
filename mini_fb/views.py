from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from .models import *
from .forms import *
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# class-based view
class ShowAllProfilesView(ListView):
    '''the view ot show all profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' #this is the context varibale to use the template

    def dispatch(self, *args: Any, **kwargs: Any):
        return super().dispatch(*args, **kwargs)
    
class ShowProfilePageView(DetailView):
    '''the view ot show a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'


class CreateProfileView(CreateView):
    '''the view to create profile'''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_creation_form'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        user_creation_form = UserCreationForm(self.request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save()
            form.instance.user = user
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, user_creation_form=user_creation_form))
        
class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    '''the view to create status message'''
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'
    context_object_name = 'status'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context
    
    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        profile = Profile.objects.get(user=self.request.user)

        form.instance.profile = profile 
        sm = form.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            image = Image(
            image_file=file,
            status_message=sm
            )
            image.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        '''Return the URL to redirect to on success.'''

        return reverse('profile', kwargs={'pk': self.request.user.profile.pk})


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

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
    
class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status'
    def get_success_url(self):
        profile = self.object.profile.pk
        return reverse('profile', kwargs={'pk':profile})
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'DeleteStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'DeleteStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        return super().form_valid(form)
    
class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    model = StatusMessage
    form_class = UpdateStatusMessageForm    
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'status'
    def get_success_url(self):
        profile = self.object.profile.pk
        return reverse('profile', kwargs={'pk':profile})

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'UpdateStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'UpdateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        user = self.request.user
        print(f"UpdateStatusMessageView user={user} profile.user={user}")
        form.instance.user = user
        return super().form_valid(form)
    
class CreateFriendView(LoginRequiredMixin, View):
    model = Profile
    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        other_profile = Profile.objects.get(pk=self.kwargs['other_pk'])
        profile.add_friend(other_profile)

        return redirect('profile', pk=profile.pk)
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'CreateFriendView.form_valid(): form={form.cleaned_data}')
        print(f'CreateFriendView.form_valid(): self.kwargs={self.kwargs}')

        user = self.request.user
        print(f"CreateFriendView user={user} profile.user={user}")
        form.instance.user = user
        return super().form_valid(form)
    
class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'ShowFriendSuggestionsView.form_valid(): form={form.cleaned_data}')
        print(f'ShowFriendSuggestionsView.form_valid(): self.kwargs={self.kwargs}')

        user = self.request.user
        print(f"ShowFriendSuggestionsView user={user} profile.user={user}")
        form.instance.user = user
        return super().form_valid(form)
    
class ShowNewsFeedView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'ShowNewsFeedView.form_valid(): form={form.cleaned_data}')
        print(f'ShowNewsFeedView.form_valid(): self.kwargs={self.kwargs}')

        user = self.request.user
        print(f"ShowNewsFeedView user={user} profile.user={user}")
        form.instance.user = user
        return super().form_valid(form)