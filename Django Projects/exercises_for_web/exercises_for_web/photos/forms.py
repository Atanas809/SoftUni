from django import forms

from exercises_for_web.common.models import PhotoLike, PhotoComment
from exercises_for_web.core.disable_fields_mixin import DisableFieldsMixin
from exercises_for_web.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }

        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Location'
                }
            ),
        }


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('photo',)

        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }

        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Location'
                }
            ),
        }


class PhotoDeleteForm(DisableFieldsMixin, PhotoEditForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.pk).delete()
            PhotoComment.objects.filter(photo_id=self.instance.pk).delete()
            self.instance.delete()

        return self.instance
