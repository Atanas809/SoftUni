from django.test import TestCase

from fitness_world.workouts.forms import DeleteWorkoutForm


class FieldsMixinTests(TestCase):
    def test_workout_delete_form_disable_fields__when_all__expect_all_to_be_disabled(self):
        form = DeleteWorkoutForm()

        disabled_fields = {
            name: field.widget.attrs[DeleteWorkoutForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            DeleteWorkoutForm.disabled_attr_name,
            disabled_fields['name']
        )
        self.assertEqual(
            DeleteWorkoutForm.disabled_attr_name,
            disabled_fields['reps']
        )
        self.assertEqual(
            DeleteWorkoutForm.disabled_attr_name,
            disabled_fields['sets']
        )
        self.assertEqual(
            DeleteWorkoutForm.disabled_attr_name,
            disabled_fields['link_to_image']
        )

    def test_workout_delete_form_disable_fields__when_name__expect_name_to_be_disabled(self):
        DeleteWorkoutForm.disabled_fields = ('name',)

        form = DeleteWorkoutForm()

        disabled_fields = {
            name: field.widget.attrs[DeleteWorkoutForm.disabled_attr_name]
            for name, field in form.fields.items()
            if DeleteWorkoutForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            DeleteWorkoutForm.disabled_attr_name,
            disabled_fields['name']
        )

        self.assertEqual(1, len(disabled_fields))

    def test_workout_delete_form_disable_fields__when_all__expect_all_to_be_required_false(self):
        form = DeleteWorkoutForm()

        required_fields = {
            name: field.required
            for name, field in form.fields.items()
        }

        self.assertFalse(required_fields['name'])
        self.assertFalse(required_fields['reps'])
        self.assertFalse(required_fields['sets'])
        self.assertFalse(required_fields['link_to_image'])

    def test_workout_delete_form_disable_fields__when_name__expect_name_to_be_required_false(self):
        DeleteWorkoutForm.disabled_fields = ('name',)
        form = DeleteWorkoutForm()

        required_fields = {
            name: field.required
            for name, field in form.fields.items()
        }

        self.assertFalse(required_fields['name'])
        self.assertTrue(required_fields['reps'])
        self.assertTrue(required_fields['sets'])
        self.assertTrue(required_fields['link_to_image'])
