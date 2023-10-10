from django.urls import path, include
from demo01.web import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('delete/student/<int:pk>/', views.delete_student, name='delete student'),
    path('school/details/<int:pk>/<slug:slug>/', views.school_details, name='school details'),
    path('student/details/<slug:slug>/', views.student_details, name='student details'),
    path('city/details/<int:pk>/<slug:slug>/', views.city_details, name='city details'),
]
