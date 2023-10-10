from django import forms

class HiddenFieldsMixin:
    hidden_fields = ()
    fields = {}

    def _set_hidden_fields(self):
        if self.hidden_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.hidden_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget = forms.HiddenInput()
