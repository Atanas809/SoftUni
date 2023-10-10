from django import forms

from gamesplay_app.games.models import Game
from gamesplay_app.mixins.hidden_fields_mixin import HiddenFieldsMixin
from gamesplay_app.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput()
        }


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(HiddenFieldsMixin, BaseProfileForm):
    hidden_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()

        return self.instance
