from django.http import HttpResponse
from django import views
from django.urls import reverse_lazy
from django.views import generic

from cbv_demo01.web.forms import CreateEmployee
from cbv_demo01.web.models import Employee


# Create your views here.

class Index(generic.TemplateView):
    template_name = 'index.html'


class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('It works LOL!')

    def post(self, request, *args, **kwargs):
        pass


class IndexTemplateView(generic.TemplateView):
    template_name = 'index-template-view.html'
    extra_context = {
        'title': 'TemplateView',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Gogo'
        return context


class IndexListView(generic.ListView):
    template_name = 'index-list-view.html'
    context_object_name = 'employees'
    model = Employee

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.request.GET.get('pattern')

        if pattern:
            queryset = queryset.filter(username__icontains=pattern)

        return queryset


class IndexDetailsView(generic.DetailView):
    template_name = 'details-view.html'
    model = Employee
    context_object_name = 'employee'
    extra_context = {
        'title': 'DetailsView',
    }


class EmployeeCreateView(generic.CreateView):
    form_class = CreateEmployee
    template_name = 'create-view.html'
    success_url = reverse_lazy('index')


class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'edit-view.html'
    success_url = reverse_lazy('list view')


class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    template_name = 'delete-view.html'
    success_url = reverse_lazy('list view')
