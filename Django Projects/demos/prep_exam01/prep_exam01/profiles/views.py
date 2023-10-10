from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from prep_exam01.albums.models import Album
from prep_exam01.core.get_user_profile import get_profile
from prep_exam01.profiles.forms import ProfileCreateForm, ProfileDeleteForm
from django.views import generic

from prep_exam01.profiles.models import Profile


# Create your views here.

class DetailsProfile(generic.DetailView):
    template_name = 'profiles/profile-details.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums_count'] = Album.objects.count()

        return context

    def get_object(self, queryset=None):
        obj = Profile.objects.first()

        return obj


class DeleteProfile(generic.DeleteView):
    template_name = 'profiles/profile-delete.html'
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        obj = Profile.objects.first()

        return obj

    def post(self, request, *args, **kwargs):
        Album.objects.all().delete()
        return super().post(request, *args, **kwargs)


class CreateProfile(generic.CreateView):
    template_name = 'common/home-no-profile.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('index')
