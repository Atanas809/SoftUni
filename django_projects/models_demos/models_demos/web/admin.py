from django.contrib import admin

from models_demos.web.models import Employees, Department, Projects, CreditCard, Category


# Register your models here.


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'age', 'company')
    list_filter = ('level', 'experience_years')
    fieldsets = (
        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'age', 'card', 'email')}),

        ('Professional experience',
         {'fields': ('level', 'experience_years',)}),

        ('Company info',
         {'fields': ('department_id', 'project_id', 'is_full_time',)}),

        ('Other info',
         {'fields': ('review', 'start_date')}),
    )

    def company(self, obj):
        return obj.department_id.name


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    pass
