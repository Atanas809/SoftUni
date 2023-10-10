from django import forms

from online_library.books.models import Book
from online_library.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            ),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL',
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class DisableFieldsMixin:
    disabled_fields = ()
    fields = {}

    def _disable_field(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['disabled'] = 'disabled'
                field.required = False


class ProfileDeleteForm(DisableFieldsMixin, ProfileBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_field()

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()

        return self.instance

