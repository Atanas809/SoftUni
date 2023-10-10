from django import forms

from web_final_exam_2022.cars.models import Car
from web_final_exam_2022.core.mixins import FieldsMixin
from web_final_exam_2022.profiles.models import Profile


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'profile_picture')

        widgets = {
            'password': forms.PasswordInput()
        }


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class EditUserForm(BaseProfileForm):
    pass


class DeleteUserForm(FieldsMixin, BaseProfileForm):
    hidden_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hide_field()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance
