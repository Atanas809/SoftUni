import random

from django.shortcuts import render, get_object_or_404, redirect

from models_demos.web.models import Employees, Department


# Create your views here.

def index(request):
    random_num = random.choice(list(range(7, 13)))
    employees = Employees.objects.all()
    employees2 = Employees.objects.all()\
        .filter(department_id=random_num)
    department = Department.objects.get(pk=10)

    # get_object_or_404(Employees, age=3030)

    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'home_page/index.html', context)


def delete_data(request, pk):
    # get_object_or_404(Department, pk=pk).delete() --> Can't delete() department because on_delete=RESTRICT
    employee = Employees.objects.filter(pk=pk)
    employee.delete()
    return redirect('index')


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }

    return render(request, 'home_page/test.html', context)
