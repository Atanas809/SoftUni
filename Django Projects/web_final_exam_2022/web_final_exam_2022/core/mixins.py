from django import forms


class FieldsMixin:
    disabled_fields = ()
    hidden_fields = ()
    fields = {}

    def _disable_field(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for current_field in fields:
            if current_field in self.fields:
                field = self.fields[current_field]
                field.widget.attrs['disabled'] = 'disabled'
                field.required = False

    def _hide_field(self):
        if self.hidden_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.hidden_fields

        for current_field in fields:
            if current_field in self.fields:
                field = self.fields[current_field]
                field.widget = forms.HiddenInput()
