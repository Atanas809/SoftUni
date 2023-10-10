from django.urls import path
from django_rest_demo.web import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('employees/', views.EmployeesListApiView.as_view(), name='api list employees'),
    path('departments/', views.DepartmentsListApiView.as_view(), name='api list departments'),
    path('demo/', views.DemoApiView.as_view(), name='api demo'),
]
