from django.shortcuts import render, redirect

from web_final_exam_2022.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm
from web_final_exam_2022.cars.models import Car


def create_car(request):
    if request.method == 'GET':
        form = CreateCarForm()

    else:
        form = CreateCarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
    }

    return render(request, 'cars/car-create.html', context)


def details_car(request, car_id):
    searched_car = Car.objects.filter(pk=car_id).get()

    context = {
        'searched_car': searched_car,
    }

    return render(request, 'cars/car-details.html', context)


def edit_car(request, car_id):
    searched_car = Car.objects.filter(pk=car_id).get()

    if request.method == 'GET':
        edit_form = EditCarForm(instance=searched_car)

    else:
        edit_form = EditCarForm(request.POST, instance=searched_car)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('catalogue page')

    context = {
        'edit_form': edit_form,
        'pk': car_id,
    }

    return render(request, 'cars/car-edit.html', context)


def delete_car(request, car_id):
    searched_car = Car.objects.filter(pk=car_id).get()

    if request.method == 'GET':
        delete_form = DeleteCarForm(instance=searched_car)

    else:
        delete_form = DeleteCarForm(request.POST, instance=searched_car)

        if delete_form.is_valid():
            delete_form.save()
            return redirect('catalogue page')

    context = {
        'delete_form': delete_form,
        'pk': car_id,
    }

    return render(request, 'cars/car-delete.html', context)
