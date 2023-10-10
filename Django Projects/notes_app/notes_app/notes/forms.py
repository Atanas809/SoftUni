from django import forms

from core.mixins import DisableFieldsMixin
from notes_app.notes.models import Note


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')

        labels = {
            'image_url': 'Link to Image',
        }


class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(DisableFieldsMixin, NoteBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
