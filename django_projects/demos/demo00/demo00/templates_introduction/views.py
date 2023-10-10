import random

from django.shortcuts import render, get_object_or_404, redirect

from demo00.templates_introduction.models import Department, Employee


# Create your views here.

class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def get_info(self):
        return f"I'm {self.age} years old {self.gender} from {self.address}"


def default_page(request):
    context = {
        'valid_links': ['variables', 'some filters', 'custom filter', 'custom tags'],
        'values': [x for x in range(10, 100, 10)]
    }

    return render(request, 'default_page.html', context)


def dtl_variables(request):
    context = {
        'page_name': 'Variables page',
        'department': 'WebDev',
        'person': Person('Ivan', 22, 'Male', 'Sofia'),
        'person_info': Person('Ivan', 22, 'Male', 'Sofia').get_info(),
        'my_dict': {
            'nested_dict': ['Ivan', 'Tonchev']
        },
        'db': 'PostgresSQL',
    }

    return render(request, 'dtl_variables.html', context)


def dtl_filters(request):
    context = {
        'first_name': 'Peter',
        'email': 'peter2444@gmail.com',
        'company': 'SoftUni',
        'numbers': [x for x in range(1, 30)],
        'names': ['Gogo', 'Peter', 'Stamat', 'Joro', 'Maria'],
        'float_num': 2.1,
        'empty_list': [],
        'value': 123456789
    }

    return render(request, 'dtl_filters.html', context)


def custom_filters(request):
    context = {
        'numbers': [x for x in range(1, 30)],
        'names': ['Gogo', 'Peter', 'Stamat', 'Joro', 'Maria'],
    }

    return render(request, 'custom_filters.html', context)


def custom_tags(request):
    context = {
        'person': Person('Ivan', 22, 'Male', 'Sofia'),
        'person_peter': Person('Peter', 30, 'Male', 'Burgas'),
    }

    return render(request, 'custom_tags.html', context)


def show_all_departments(request):
    departments = Department.objects.all()
    employees = Employee.objects.exclude(pk=2)
    search_employee = get_object_or_404(Employee, pk=5)
    lookup_filters = Employee.objects.filter(age__gte=22)

    context = {
        'departments': departments,
        'employees': employees,
        'employee_with_id': search_employee,
        'with_lookup': lookup_filters
    }

    return render(request, 'show_departments.html', context)


def delete_obj(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('show departments')


def absolute_url(request, pk):
    context = {
        'department': get_object_or_404(Department, pk=pk)
    }

    return render(request, 'get_absolute_url.html', context)
