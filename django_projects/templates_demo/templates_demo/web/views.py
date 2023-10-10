import datetime
import random

from django.shortcuts import render, redirect


# Create your views here.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


def index(request):
    context = {
        'title': 'softUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Peter', 22),
        'student_info': Student('Gogo', 19).get_info(),
        'now': datetime.datetime.now(),
        'students': ['Gogo', 'Gogo', 'Gogo', 'Maria', 'Peter', 'Peter', 'Dimo'],
        # 'students': [],
        'numbers': [x for x in range(1, 30)],
    }

    return render(request, 'index.html', context)


def redirection(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')
