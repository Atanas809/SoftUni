from django import forms

from core.mixins import FieldsMixin
from prep_exam01.albums.models import Album
from prep_exam01.profiles.models import Profile


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


class ProfileDeleteForm(FieldsMixin, ProfileBaseForm):
    hidden_fields = '__all__'
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._hide_field()
        self._disable_field()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance
