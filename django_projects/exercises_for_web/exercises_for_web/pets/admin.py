from django.contrib import admin

from exercises_for_web.pets.models import Pet


# Register your models here.


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)

