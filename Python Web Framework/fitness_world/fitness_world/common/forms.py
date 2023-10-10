from django import forms

from fitness_world.common.models import CommentPhoto
from fitness_world.core.mixins import FieldsMixin


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = CommentPhoto
        fields = ('text',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = CommentPhoto
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Comment...',
                    'cols': 40,
                    'rows': 10,
                }
            ),
        }


class CommentEditForm(CommentBaseForm):
    pass


class CommentDeleteForm(FieldsMixin, CommentBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class SearchForm(forms.Form):
    workout_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by workout name...',
            }
        )
    )


