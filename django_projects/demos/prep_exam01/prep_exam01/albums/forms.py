from django import forms

from core.mixins import FieldsMixin
from prep_exam01.albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL',
        }

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(FieldsMixin, AlbumBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
