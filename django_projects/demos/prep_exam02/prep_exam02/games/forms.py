from django import forms

from prep_exam02.core.mixins import FieldsMixin
from prep_exam02.games.models import Game


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL',
        }


class GameCreateForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(FieldsMixin, GameBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
