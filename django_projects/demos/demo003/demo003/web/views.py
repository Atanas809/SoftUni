from django.shortcuts import render, redirect

from demo003.web.forms import StudentForm, StudentModelForm
from demo003.web.models import Student


# Create your views here.


def student_form(request):
    name = None
    if request.method == "GET":
        form = StudentForm()
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'exercise_one/student_form.html', context)


def student_model_form(request):
    name = None
    if request.method == "GET":
        form = StudentModelForm()
    else:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            return redirect('edit', name=name)

    context = {
        'form': form,
    }

    return render(request, 'exercise_one/student_model_form.html', context)


def edit(request, name):
    student = Student.objects.filter(name=name).first()
    if request.method == 'GET':
        form = StudentModelForm(instance=student)
    else:
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student form')

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'exercise_one/edit_page.html', context)
