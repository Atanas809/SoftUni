from django import forms

from forms_demo.web.models import Person


class PersonForm(forms.Form):
    DROP = (
        ('Junior', 'Junior'),
        ('Regular', 'Regular'),
        ('Senior', 'Senior'),
    )

    your_name = forms.CharField(
        max_length=30,
    )

    age = forms.IntegerField(
        required=False,
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter email',
                'class': 'form-controls',
            },
        ),
    )

    url = forms.CharField(
        widget=forms.URLInput(),
    )

    secret = forms.CharField(
        widget=forms.PasswordInput(),
    )

    story = forms.CharField(
        widget=forms.Textarea(),
        required=False,
    )

    level = forms.ChoiceField(
        choices=DROP,
    )

    level2 = forms.ChoiceField(
        choices=DROP,
        widget=forms.RadioSelect(),
    )

    multiple = forms.ChoiceField(
        choices=DROP,
        widget=forms.SelectMultiple(),
    )

    full_time = forms.ChoiceField(
        widget=forms.CheckboxInput(),
    )


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
