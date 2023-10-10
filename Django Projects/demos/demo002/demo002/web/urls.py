from django.urls import path, include
from demo002.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', include([
        path('students/', views.show_students, name='show students'),
        path('courses/', views.show_courses, name='show courses'),
    ])),
    path('student/info/<int:pk>/', views.student_info, name='student info'),
    path('course/info/<int:pk>/<slug:slug>/', views.course_info, name='course info'),
    path('delete/student/<int:pk>', views.delete_student, name='delete student'),
]
