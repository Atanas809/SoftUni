from django import forms

from my_music_app.albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                },
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            )
        }
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class DisableFieldsMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == "__all__":
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'
                field.required = False


class AlbumDeleteForm(DisableFieldsMixin, AlbumBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
