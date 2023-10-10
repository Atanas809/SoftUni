from django.urls import path

from common_web_tools.web.views import index, RegisterStudent, ListStudents, EditStudentView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterStudent.as_view(), name='register student'),
    path('show/', ListStudents.as_view(), name='show students'),
    path('edit/<int:pk>/', EditStudentView.as_view(), name='edit student'),
]


from .signals import *
