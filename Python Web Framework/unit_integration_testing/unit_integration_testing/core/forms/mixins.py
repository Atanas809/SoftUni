class DisableFieldsMixin:
    disabled_attr_name = 'disabled'
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == "__all__":
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs[self.disabled_attr_name] = self.disabled_attr_name
                field.required = False
