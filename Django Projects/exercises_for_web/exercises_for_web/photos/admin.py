from django.contrib import admin

from exercises_for_web.photos.models import Photo


# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication_date', 'all_tagged_pets')

    @staticmethod
    def all_tagged_pets(obj):
        pets = obj.tagged_pets.all()

        if not pets:
            return 'No pets tagged'

        return ', '.join(pet.name for pet in pets)
