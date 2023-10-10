from django import forms

from unit_integration_testing.core.forms.mixins import DisableFieldsMixin
from unit_integration_testing.web.models import Profile


class ProfileDeleteForm(DisableFieldsMixin, forms.ModelForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Profile
        fields = '__all__'
