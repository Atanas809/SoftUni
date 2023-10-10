import random

from django.shortcuts import render, redirect

from demo003.forms_web.forms import UserForm, CourseModelForm
from demo003.forms_web.models import Course


# Create your views here.

def get_random_course_slug():
    courses = Course.objects.all()

    course = random.choice(courses)

    return course.slug


def index(request):
    return redirect('model form')


def register_form(request):
    username = None
    if request.method == "GET":
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

    context = {
        'form': form,
        'username': username,
    }

    return render(request, 'exercise_two/register_page.html', context)


def register_model_form(request):
    course_name = None
    if request.method == "GET":
        model_form = CourseModelForm()
    else:
        model_form = CourseModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            course_slug = get_random_course_slug()
            return redirect('update course', slug=course_slug)

    context = {
        'model_form': model_form,
        'course_name': course_name,
    }

    return render(request, 'exercise_two/model_form_page.html', context)


def update_course(request, slug):
    course = Course.objects.get(slug=slug)

    if request.method == "GET":
        model_form = CourseModelForm(instance=course)
    else:
        model_form = CourseModelForm(request.POST, instance=course)
        if model_form.is_valid():
            model_form.save()

    context = {
        'course': course,
        'model_form': model_form,
    }

    return render(request, 'exercise_two/update_course.html', context)
