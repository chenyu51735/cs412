from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from .models import *
from .forms import *
from typing import Any
# class-based view
class ShowAllProfilesView(ListView):
    '''the view ot show all profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' #this is the context varibale to use the template

class ShowProfilePageView(DetailView):
    '''the view ot show a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    '''the view to create profile'''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'


class CreateStatusMessageView(CreateView):
    '''the view to create status message'''
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'
    context_object_name = 'status'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        profile = Profile.objects.get(pk=self.kwargs['pk'])

        form.instance.profile = profile 
        sm = form.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            image = Image(
            image_file=file,
            status_message=sm
            )
            image.save()
        # delegate work to superclass version of this method

        return super().form_valid(form)

    def get_success_url(self) -> str:
        '''Return the URL to redirect to on success.'''

        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return reverse('profile', kwargs={'pk':profile.pk})


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

class DeleteStatusMessageView(DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status'
    def get_success_url(self):
        profile = self.object.profile.pk
        return reverse('profile', kwargs={'pk':profile})
    
class UpdateStatusMessageView(UpdateView):
    model = StatusMessage
    form_class = UpdateStatusMessageForm    
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'status'
    def get_success_url(self):
        profile = self.object.profile.pk
        return reverse('profile', kwargs={'pk':profile})
    
class CreateFriendView(View):
    model = Profile
    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        other_profile = Profile.objects.get(pk=self.kwargs['other_pk'])
        profile.add_friend(other_profile)

        return redirect('profile', pk=profile.pk)
    
class ShowFriendSuggestionsView(DetailView):
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'