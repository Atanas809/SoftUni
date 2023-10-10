from django.urls import reverse_lazy

from fitness_world.workouts.models import Workout
from tests import BaseTestCase


class CreateWorkoutTests(BaseTestCase):
    def test_create_workout__when_creates_new_entity__expect_workout_to_have_correct_user(self):
        user1 = self.create_and_login_user()
        self.client.logout()
        user2 = self.create_and_login_user({
            'username': 'ivan231',
            'email': 'ivan231@abv.bg',
            'password': 'Ivancho@34',
        })

        self.client.post(
            reverse_lazy('create workout'),
            data={
                'name': 'squads',
                'reps': 4,
                'sets': 9,
                'link_to_image': 'https://upload.wikimedia.org/wikipedia/c4',
            }
        )

        workout = Workout.objects.filter(pk=1).get()

        self.assertEqual(user2, workout.user)
        self.assertNotEqual(user1, workout.user)
