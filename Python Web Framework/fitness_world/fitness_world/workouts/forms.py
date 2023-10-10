from django import forms

from fitness_world.core.mixins import FieldsMixin
from fitness_world.workouts.models import Workout


class WorkoutBaseForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ('slug', 'user')

        labels = {
            'name': 'Name',
            'link_to_image': 'Link to Image',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Workout Name',
                }
            ),

            'reps': forms.NumberInput(
                attrs={
                    'placeholder': 'Reps',
                }
            ),

            'sets': forms.NumberInput(
                attrs={
                    'placeholder': 'Sets',
                }
            ),

            'link_to_image': forms.URLInput(
                attrs={
                    'placeholder': 'Image Link'
                }
            ),
        }


class WorkoutCreateForm(WorkoutBaseForm):
    pass


class WorkoutEditForm(WorkoutBaseForm):
    pass


class DeleteWorkoutForm(FieldsMixin, WorkoutBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
