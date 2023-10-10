from django.http import HttpResponse
from django import forms
from django import views
from django.views import generic

from cbv_introduction.web_cbv.models import Student


# Create your views here.


class IndexView(views.View):

    def get(self, request):
        return HttpResponse("It works!!!")

    def post(self, request):
        pass


class IndexViewWithTemplate(generic.TemplateView):
    template_name = 'index-template-view.html'
    extra_context = {
        'text': 'TemplateView',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context


class IndexViewWithListView(generic.ListView):
    model = Student
    template_name = 'index-template-view.html'
    context_object_name = 'students'
    extra_context = {'text': 'ListView'}

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern)

        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


class IndexViewWithDetailsView(generic.DetailView):
    model = Student
    template_name = 'student-details.html'
    context_object_name = 'student'


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Last Name',
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Age',
                }
            )
        }


class IndexViewWithCreateView(generic.CreateView):
    # First way:
    # model = Student
    # fields = '__all__'
    template_name = 'create-student.html'

    # Second way:
    form_class = StudentCreateForm

    # Third way:
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['placeholder'] = 'Enter ' + name
    #
    #     return form


class IndexViewWithUpdateView(generic.UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'edit-student.html'
    context_object_name = 'student'
