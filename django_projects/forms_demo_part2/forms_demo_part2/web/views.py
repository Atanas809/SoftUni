from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_demo_part2.web.forms import AnimalModelForm, AnimalForm
from forms_demo_part2.web.models import Animal


# Create your views here.

def show_animals(request):
    animals = Animal.objects.all()

    context = {
        'animals': animals,
    }

    return render(request, 'show-animals.html', context)


def index(request):
    if request.method == "GET":
        form = AnimalModelForm()
    else:
        form = AnimalModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('show animals')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)
