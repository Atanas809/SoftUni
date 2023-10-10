from django import forms
from django.contrib.auth import get_user_model

from fitness_world.common.models import LikePhoto, CommentPhoto
from fitness_world.core.mixins import FieldsMixin
from fitness_world.photos.models import Photo

UserModel = get_user_model()


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user', 'date_of_publication',)

        labels = {
            'music_link': 'Music Link',
            'workout': 'Workout Type',
        }

        widgets = {
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Location'
                }
            ),

            'caption': forms.Textarea(
                attrs={
                    'placeholder': 'Caption',
                }
            ),

            'music_link': forms.URLInput(
                attrs={
                    'placeholder': 'Link to music'
                }
            ),

        }


class CreatePhotoForm(PhotoBaseForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['workout'].queryset = user.workout_set.all()


class EditPhotoForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('user', 'image', 'date_of_publication',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['workout'].queryset = user.workout_set.all()


class DeletePhotoForm(FieldsMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs['instance'].user
        self.fields['workout'].queryset = user.workout_set.all()
        self._disable_field()

    def save(self, commit=True):
        if commit:
            LikePhoto.objects.filter(photo_id=self.instance.pk).delete()
            CommentPhoto.objects.filter(photo_id=self.instance.pk).delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = Photo
        exclude = ('user', 'image', 'date_of_publication',)

