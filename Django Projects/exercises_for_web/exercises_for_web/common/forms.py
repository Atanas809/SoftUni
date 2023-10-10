from django import forms

from exercises_for_web.common.models import PhotoComment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 40,
                    'cols': 10,
                    'placeholder': 'Add comment...'
                }
            )
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...',
            }
        ),
    )
