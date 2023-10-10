from django.contrib import admin

from demo01.web.models import Student, School, City, Address


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'school_name')
    prepopulated_fields = {'slug': ('last_name',)}
    fieldsets = (
        ('Student Info',
         {'fields': (
             'first_name',
             'last_name',
             'age',
             'level',
         )}),

        ('Additional Info',
         {'classes': ('collapse',),
          'fields': (
              'school',
              'good_grades',
              'slug',
         )})
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')
    prepopulated_fields = {'slug': ('postal_code',)}


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')