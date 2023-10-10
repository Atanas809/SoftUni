from django.contrib import admin

from fitness_world.workouts.models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'reps', 'sets',)
    list_filter = ('name',)
    search_fields = ("name__icontains",)
    list_per_page = 5
