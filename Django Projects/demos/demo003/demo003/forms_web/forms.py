from django import forms

from demo003.forms_web.models import Course
from demo003.forms_web.validations import password_check


class UserForm(forms.Form):
    MAX_USERNAME_LENGTH = 40
    MAX_ADDRESS_LENGTH = 50

    username = forms.CharField(
        max_length=MAX_USERNAME_LENGTH,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter username',
            }
        )
    )

    email = forms.EmailField()

    secret = forms.CharField(
        validators=(password_check, ),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
            }
        ),
    )

    address = forms.CharField(
        max_length=MAX_ADDRESS_LENGTH,
        required=False,
    )

    about = forms.CharField(
        widget=forms.Textarea(),
        required=False,
    )


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'company': forms.RadioSelect()
        }

        labels = {
            'company': 'Choose company'
        }
