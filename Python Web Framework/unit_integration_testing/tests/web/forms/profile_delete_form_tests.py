from django.test import TestCase

from unit_integration_testing.web.forms import ProfileDeleteForm


class ProfileDeleteFormTests(TestCase):
    def test_profile_delete_form_disable_fields__when_all__expect_all_to_be_disabled(self):
        form = ProfileDeleteForm()

        disabled_fields = {
            name: field.widget.attrs[ProfileDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            ProfileDeleteForm.disabled_attr_name,
            disabled_fields['name']
        )
        self.assertEqual(
            ProfileDeleteForm.disabled_attr_name,
            disabled_fields['age']
        )
        self.assertEqual(
            ProfileDeleteForm.disabled_attr_name,
            disabled_fields['egn']
        )

    def test_profile_delete_form_disable_fields__when_name__expect_name_to_be_disabled(self):
        ProfileDeleteForm.disabled_fields = ('name',)

        form = ProfileDeleteForm()

        disabled_fields = {
            name: field.widget.attrs[ProfileDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
            if ProfileDeleteForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            ProfileDeleteForm.disabled_attr_name,
            disabled_fields['name']
        )

        self.assertEqual(1, len(disabled_fields))

    def test_profile_delete_form_disable_fields__when_all__expect_all_to_be_required_false(self):
        form = ProfileDeleteForm()

        required_fields = {
            name: field.required
            for name, field in form.fields.items()
        }

        self.assertFalse(required_fields['name'])
        self.assertFalse(required_fields['age'])
        self.assertFalse(required_fields['egn'])

    def test_profile_delete_form_disable_fields__when_name__expect_name_to_be_required_false(self):
        ProfileDeleteForm.disabled_fields = ('name',)
        form = ProfileDeleteForm()

        required_fields = {
            name: field.required
            for name, field in form.fields.items()
        }

        self.assertFalse(required_fields['name'])
        self.assertTrue(required_fields['age'])
        self.assertTrue(required_fields['egn'])
