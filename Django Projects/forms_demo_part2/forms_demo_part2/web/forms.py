from django import forms
from django.core.exceptions import ValidationError

from forms_demo_part2.web.form_validations import possible_relations
from forms_demo_part2.web.models import Animal
from forms_demo_part2.web.validators import first_char_is_upper


class AnimalForm(forms.Form):
    ANIMAL_TYPE = (
        ('Mammals', 'Mammals'),
        ('Fishes', 'Fishes'),
        ('Birds', 'Birds'),
        ('Reptiles', 'Reptiles'),
    )

    name = forms.CharField(
        validators=(first_char_is_upper,),
    )

    type = forms.ChoiceField(
        choices=ANIMAL_TYPE,
        widget=forms.RadioSelect(
        )
    )


class AnimalModelForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'type': forms.RadioSelect()
        }

    def clean(self):
        return super().clean()

    def clean_name(self):
        animal_name = self.cleaned_data['name']
        first_char_is_upper(animal_name)
        return animal_name

    def clean_type(self):
        animal_type = self.cleaned_data['type']
        possible_relations(animal_type)
        return animal_type
