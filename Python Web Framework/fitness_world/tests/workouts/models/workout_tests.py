from tests import BaseTestCase


class WorkoutTests(BaseTestCase):
    def test_workout_model__when_creating_new_workout__expect_slug_to_be_like_name(self):
        user = self.create_and_login_user()

        workout = self.create_workouts(user, count=1)[0]

        expected = workout.name.lower().replace(' ', '-')
        result = workout.slug

        self.assertEqual(expected, result)
