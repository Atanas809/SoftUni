from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from common_web_tools.web.forms import RegisterStudentForm, EditProfileForm
from common_web_tools.web.models import Student, Profile

VISITS_SESSION_KEY = 'VISITS_SESSION_KEY'


def index(request):
    number_of_visits = request.session.get('VISITS_SESSION_KEY')

    return HttpResponse(f'Visits: {number_of_visits}')


class RegisterStudent(generic.CreateView):
    template_name = 'register-students.html'
    form_class = RegisterStudentForm
    success_url = reverse_lazy('show students')


class ListStudents(generic.ListView):
    template_name = 'list-students.html'
    model = Student


class EditStudentView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit-student.html'
    model = Profile
    success_url = reverse_lazy('show students')
