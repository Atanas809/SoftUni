from django.shortcuts import render, redirect

from demo002.web.models import Student, Course


# Create your views here.


def index(request):
    return render(request, 'index.html')


def show_students(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }

    return render(request, 'show_students.html', context)


def show_courses(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'show_courses.html', context)


def student_info(request, pk):
    student = Student.objects.get(pk=pk)

    context = {
        'student': student,
    }

    return render(request, 'student_info.html', context)


def course_info(request, pk, slug):
    course = Course.objects.get(slug=slug)

    context = {
        'course': course,
    }

    return render(request, 'course_info.html', context)


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('show students')
