from django import forms

from petstagram.common.models import PhotoComment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text', )

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': "Add comment...",
                    'rows': 10,
                    'cols': 40,
                }
            ),
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Search by pet name...",
            }
        )
    )

