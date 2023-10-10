from django.contrib import admin

from petstagram.pets.models import Pet


# Register your models here.


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth')
