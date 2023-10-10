from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'pets')

    @staticmethod
    def pets(obj):
        all_pets = obj.tagged_pets.all()
        if all_pets:
            return ', '.join([pet.name for pet in all_pets])
        return 'No pets'
