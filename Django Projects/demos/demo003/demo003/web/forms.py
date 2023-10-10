from django import forms

from demo003.web.models import Student


class StudentForm(forms.Form):
    CHOICES = (
        ('Junior', 'Junior'),
        ('Mid', 'Mid'),
        ('Regular', 'Regular'),
        ('Senior', 'Senior'),
        ('Other', 'Other'),
    )

    your_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter name',
            },
        )
    )

    age = forms.IntegerField(
        min_value=0,
        initial=0,
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
        required=False,
    )

    secret = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=10,
    )

    url = forms.CharField(
        widget=forms.URLInput(),
        required=False,
    )

    skills = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'cols': 40,
                'rows': 10,
                'placeholder': 'Add comment',
            }
        ),
        required=False,

    )

    select_list = forms.ChoiceField(
        choices=CHOICES,
    )

    check_box = forms.BooleanField()

    radio_select = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=CHOICES,
    )


class StudentModelForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            ),
        }
