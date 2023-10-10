from django import forms

from gamesplay_app.games.models import Game
from gamesplay_app.mixins.disable_fields_mixin import DisabledFieldsMixin


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL',
        }


class CreateGameForm(GameBaseForm):
    pass


class EditGameForm(GameBaseForm):
    pass


class DeleteGameForm(DisabledFieldsMixin, GameBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
