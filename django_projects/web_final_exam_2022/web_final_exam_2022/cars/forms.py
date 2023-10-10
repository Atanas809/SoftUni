from django import forms

from web_final_exam_2022.cars.models import Car
from web_final_exam_2022.core.mixins import FieldsMixin


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'car_type': 'Type',
            'image_url': 'Image URL',
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(FieldsMixin, BaseCarForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
