from django.contrib import admin

from demo003.forms_web.models import Course, Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
