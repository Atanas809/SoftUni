from django.contrib import admin

from demo003.web.models import Course, Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
