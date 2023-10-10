from django import forms

from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class HiddenFieldsMixin:
    hidden_fields = ()
    fields = {}
    
    def _set_hidden_fields(self):
        if self.hidden_fields == "__all__":
            fields = self.fields.keys()
        else:
            fields = self.hidden_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget = forms.HiddenInput()


class ProfileDeleteForm(HiddenFieldsMixin, ProfileBaseForm):
    hidden_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance

