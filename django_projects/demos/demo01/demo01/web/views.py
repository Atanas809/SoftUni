from django.shortcuts import render, get_object_or_404, redirect

from demo01.web.models import Student, School, City


# Create your views here.


def index(request):
    students = Student.objects.all()
    students_under_19 = Student.objects.filter(age__lt=19)
    get_student_by_id = get_object_or_404(Student, pk=3)

    context = {
        'all_students': students,
        'students_under_19': students_under_19,
        'student_by_id': get_student_by_id,
    }

    return render(request, 'index.html', context)


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('home page')


def school_details(request, pk, slug):
    school = School.objects.get(pk=pk, slug=slug)
    school_name = school.name

    context = {
        'school': school,
        'school_name': school_name,
        'city': school.city,
    }

    return render(request, 'school_details.html', context)


def student_details(request, slug):
    student = Student.objects.get(slug=slug)

    context = {
        'student': student,
        'city': student.school.city,
    }

    return render(request, 'student_details.html', context)


def city_details(request, pk, slug):
    city = City.objects.get(pk=pk, slug=slug)

    context = {
        'city': city,
    }

    return render(request, 'city_details.html', context)
