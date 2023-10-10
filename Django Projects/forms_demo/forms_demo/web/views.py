from django.shortcuts import render

from forms_demo.web.forms import PersonForm, PersonModelForm
from forms_demo.web.models import Person


# Create your views here.


def index_form(request):
    name = None
    if request.method == "GET":
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )

    context = {
        'form': PersonForm(),
        'name': name,
    }

    return render(request, 'index_forms.html', context)


def index_model_form(request):
    if request.method == 'GET':
        form = PersonModelForm()
    else:
        form = PersonModelForm(request.POST)
        if form.is_valid():
           form.save()

    context = {
        'form': form
    }

    return render(request, 'index_model_forms.html', context)