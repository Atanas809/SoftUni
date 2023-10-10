from django.contrib import admin

from fitness_world.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image', 'date_of_publication', 'workouts')
    ordering = ('date_of_publication',)
    list_per_page = 5

    @staticmethod
    def workouts(obj):
        all_workouts = obj.workout.all()
        if all_workouts:
            return ', '.join([w.name for w in all_workouts])
        return 'No added workouts'
