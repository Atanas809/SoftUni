from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from unit_integration_testing.web.models import Profile


class ProfileListView(generic.ListView):
    template_name = 'show-profiles.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['profiles_count'] = self.object_list.count()
        context['username'] = self.request.user.username or 'Anonymous'
        context['query'] = self.request.GET.get('query')

        return context


class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'create.html'
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('show profiles')
