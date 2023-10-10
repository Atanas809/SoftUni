from rest_framework import generics as rest_views
from django.views import generic as views
from rest_framework import views as rest_base_views
from rest_framework import serializers
from rest_framework.response import Response

from django_rest_demo.web.models import Employee, Department
from django_rest_demo.web.serializers import EmployeeSerializer, DepartmentSerializer, ShortEmployeeSerializer, \
    ShortDepartmentSerializer, DemoSerializer


# Server-side rendering, i.e. the result is rendered HTML
class EmployeeListView(views.ListView):
    model = Employee
    template_name = ''


# JSON serialization i.e. parse models into JSON
class EmployeesListApiView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = self.queryset
        department_id = self.request.query_params.get('department_id')

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset.all()


class DepartmentsListApiView(rest_views.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DemoApiView(rest_base_views.APIView):
    def get(self, request):
        employees = Employee.objects.all()
        departments = Department.objects.all()
        body = {
            'employees': employees,
            'employees_count': employees.count(),
            'departments': departments,
            'first_department': departments.first(),
            'departments_names': departments,
        }

        serializer = DemoSerializer(body)

        # Not 'HttpResponse' (this comes from Django)
        # 'Response' comes from DRF(Django REST Framework)
        return Response(serializer.data)


class IndexView(views.TemplateView):
    template_name = 'index.html'
